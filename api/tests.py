from django.test import TestCase
from api.models import Person, Employee, update_field
from api.xml_parse import parse_hires
from bpm.xml_request import get_talented_xml
from datetime import date
from api.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
import os


# Create your tests here.
class PersonTestCase(TestCase):
    def setUp(self):
        jon = Employee.objects.create(first_name="Jon", last_name="Snow")
        arya = Person.objects.create(first_name="Arya", last_name="Stark")
        jon.employee_id = "SN12345"
        jon.talented_id = 12345
        jon.save()
        arya.save()

    def test_find_employee(self):
        people = Person.objects.all()
        self.assertEqual(people.count(), 2)
        newjon = Employee.objects.get(first_name="Jon")
        self.assertEqual(newjon.employee_id, "SN12345")

    def test_person_exists(self):
        self.assertIs(Person.person_exists(12345), True)

    def test_update_field(self):
        update_jon = Employee.objects.get(talented_id=12345)
        update_field(update_jon, "middle_name", "Stark")
        final_jon = Employee.objects.get(talented_id=12345)
        self.assertEqual(final_jon.middle_name, "Stark")

    def test_parse_hires(self):
        if os.environ.get("CIRCLECI") == "true":
            get_talented_xml()
        parse_hires()
        emp = Employee.objects.get(talented_id=13345)
        self.assertEqual(emp.first_name, "Yenni")
        self.assertEqual(emp.ethnicity, "Hispanic")
        self.assertIs(emp.race_asian, False)
        self.assertEqual(emp.gender, "F")
        self.assertEqual(emp.marked_as_hired, date(2017, 1, 23))
        emp2 = Employee.objects.get(talented_id=13475)
        self.assertEqual(emp2.first_name, "Berhana")
        self.assertIs(emp2.race_white, False)
        emp3 = Employee.objects.get(talented_id=13325)
        self.assertEqual(emp3.first_name, "Jennifer")
        self.assertIs(emp3.race_white, True)
        self.assertIs(emp.race_asian, False)


class RestTestCase(TestCase):
    def setUp(self):
        tyrion = Employee.objects.create(first_name="Tyrion", last_name="Lanister")
        tyrion.save()

    def test_json(self):
        tyrion = Employee.objects.get(first_name="Tyrion")
        t_serial = EmployeeSerializer(tyrion)
        json_string = JSONRenderer().render(t_serial.data)
        stream = BytesIO(json_string)
        data = JSONParser().parse(stream)
        self.assertEqual(data["first_name"], "Tyrion")
