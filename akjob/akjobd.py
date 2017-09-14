""" The akjob daemon. """

import os
import sys
import argparse
import pid
import daemon
from time import sleep

try:
    from akjob_logger import AkjobLogging
except ModuleNotFoundError:  # noqa  pyflake/flake8 doesn't have this builtin.
    from akjob.akjob_logger import AkjobLogging


""" Notes:
python-daemon asks for pylockfile but that package is depreciated. Instead I'm
using pid which is python-daemon compatible.
"""


# Django has to be setup separately to disable the running of akjobd on django
# startup thereby causing an infinite loop.
def setup_django():
    os.environ['AKJOB_START_DAEMON'] = 'False'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "akbash.settings")
    import django
    django.setup()
    global Job
    from akjob.models import Job

# Set up logging
def setup_logging():
    global logger
    akjob_logging = AkjobLogging(name="akjob.akjobd", logfilename="akjobd.log")
    logger = akjob_logging.get_logger()

# A different logger to run inside the daemon process.
def get_daemon_logger():
    akjob_logging = AkjobLogging(
        name="akjob.akjobd.daemon",
        logfilename="akjobd.daemon.log",
    )
    return akjob_logging.get_logger()


# setup piddir and pidname from command line arguments.
def parse_args():
    global args
    global piddir
    global pidfile
    # global basedir
    parser = argparse.ArgumentParser()
    parser.add_argument("action",
                        choices=["start", "stop", "restart"],
                        help="Action to perform.")
    parser.add_argument("-pd", "--piddir",
                        required=True,
                        help="The directory used to store the pid file.")
    parser.add_argument("-pn", "--pidname",
                        required=True,
                        help="The name of the pid file.")
    # parser.add_argument("-ld", "--logdir",
    #                     help="The directory used to store the log file.")
    # parser.add_argument("-ln", "--logname",
    #                     help="The name of the log file.")
    # parser.add_argument("-bd", "--basedir",
    #                     help="The django site's base directory.")
    args = parser.parse_args()

    piddir = args.piddir
    pidfile = args.pidname
    # basedir = args.basedir


def worker(idnum):
    global dlog
    job = Job.objects.get(id=idnum)
    dlog.info("Starting job " + str(job.id) + ", " + job.name)
    try:
        job.run()
    except Exception as inst:
        dlog.error("Something went wrong with Job " + str(job.id) + ", " +
                   job.name + "\n    " + str(inst))

def loop_through_jobs():
    for j in Job.objects.all():
        worker(j.id)
        # sleep(1)

# maybe learn how to catch the termination signal so daemon shutdown can be
# logged.
def daemonize():
    with daemon.DaemonContext(
            pidfile=pid.PidFile(pidname=pidfile, piddir=piddir)):
        global dlog
        dlog = get_daemon_logger()
        while True:
            loop_through_jobs()
            sleep(60)


def stop_daemon(pid):
    logger.info("Stopping Daemon. Sending SIGTERM to pid " + str(pid))
    os.kill(pid, 15)  # 15 = SIGTERM - "Software termination signal"

def start_daemon():
    logger.info("Starting the akjob daemon.")
    daemonize()

# To get the pid module to do this for me proved tricky. I'll get it myself.
def get_pid_from_pidfile(piddir=piddir, pidfile=pidfile):
    "Read the pid in the pidfile."
    filename = os.path.abspath(os.path.join(piddir, pidfile))
    with open(filename, "r") as fh:
        fh.seek(0)
        pid_str = fh.read(16).split("\n", 1)[0].strip()
        return int(pid_str)

# Before the daemon starts it checks the pid file but I can't monitor the
# results so here I'm doing a pre-check on the pidfile.
def pid_precheck(piddir=piddir, pidfile=pidfile):
    "Check the pidfile."
    # logger.debug("Pre-checking PID file.")
    pidcheck = pid.PidFile(pidname=pidfile, piddir=piddir)
    pidstatus = None
    try:
        pidstatus = pidcheck.check()
        if pidstatus:
            logger.info(pidstatus)
        if pidstatus == "PID_CHECK_NOFILE":
            return pidstatus
    except pid.PidFileAlreadyRunningError as err:
        logger.info(err)
        return "AlreadyRunning"
    except:
        logger.error('Unknown pid related error: ' + str(sys.exc_info()[1:2]))
        raise SystemExit

def main():
    setup_logging()
    parse_args()
    status = pid_precheck()
    if status == "AlreadyRunning":
        if args.action == "stop":
            stop_daemon(get_pid_from_pidfile())
        elif args.action == "restart":
            stop_daemon(get_pid_from_pidfile())
            sleep(1)
            start_daemon()
        raise SystemExit
    if args.action == "stop":
        if status == "PID_CHECK_NOFILE":
            logger.info("Stop command given but the pid file wasn't found.")
        else:
            stop_daemon(get_pid_from_pidfile())
            raise SystemExit
    elif args.action == "start":
        start_daemon()
    elif args.action == "restart":
        logger.info("restart command given but the pid file wasn't found.")
        start_daemon()
    else:
        logger.error("Didn't receive start or stop command.")


if __name__ == '__main__':
    setup_django()
    main()
