from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Vendor Classes

class VendorType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    vendor_type = models.ForeignKey(VendorType, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % self.name


# Person Classes

class Person(models.Model):
    TYPES = (
        ("Contractor", "Contractor"),
        ("Employee", "Employee"),
    )
    type = models.CharField(max_length=16, choices=TYPES)
    first_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    badge_number = models.IntegerField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    race_white = models.BooleanField(default=False)
    race_asian = models.BooleanField(default=False)
    race_black = models.BooleanField(default=False)
    race_islander = models.BooleanField(default=False)
    race_american_indian = models.BooleanField(default=False)
    ethnicity = models.CharField(max_length=50, blank=True)
    hqt = models.CharField(max_length=16, blank=True)
    ssn = models.CharField(max_length=9, blank=True)
    tcp_id = models.IntegerField(null=True)
    talented_id = models.IntegerField(null=True)
    is_onboarded = models.BooleanField(default=False)
    onboarded_date = models.DateTimeField(null=True, blank=True)
    onboarded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_tcp_fingerprinted = models.BooleanField(default=False)
    tcp_fingerprinted_date = models.DateTimeField(null=True, blank=True)
    tcp_fingerprinted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="tcp_fingerprinted_user")
    is_badge_created = models.BooleanField(default=False)
    badge_created_date = models.DateTimeField(null=True, blank=True)
    badge_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="badge_created_user")
    is_emp_record_created = models.BooleanField(default=False)
    emp_record_created_date = models.DateTimeField(null=True, blank=True)
    emp_record_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="emp_record_created_user")
    is_position_linked = models.BooleanField(default=False)
    position_linked_date = models.DateTimeField(null=True, blank=True)
    position_linked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="position_linked_user")
    is_visions_account_needed = models.BooleanField(default=False)
    is_visions_account_created = models.BooleanField(default=False)
    visions_account_created_date = models.DateTimeField(null=True, blank=True)
    visions_account_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="visions_account_created_user")
    is_synergy_account_needed = models.BooleanField(default=False)
    is_synergy_account_created = models.BooleanField(default=False)
    synergy_account_created_date = models.DateTimeField(null=True, blank=True)
    synergy_account_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="synergy_account_created_user")
    is_ad_account_created = models.BooleanField(default=False)
    ad_account_created_date = models.DateTimeField(null=True, blank=True)
    ad_account_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="ad_account_created_user")
    is_cell_phone_needed = models.BooleanField(default=False)
    is_cell_phone_created = models.BooleanField(default=False)
    cell_phone_created_date = models.DateTimeField(null=True, blank=True)
    cell_phone_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cell_phone_created_user")
    is_desk_phone_created = models.BooleanField(default=False)
    desk_phone_created_date = models.DateTimeField(null=True, blank=True)
    desk_phone_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="desk_phone_created_user")

    # Convieniece function to verify if an Employee exists by talented_id
    @staticmethod
    def person_exists(tid):
        qs = Person.objects.filter(talented_id=tid)
        if qs.exists():
            return True
        else:
            return False

    def personType(self):
        try:
            if self.contractor.id:
                return "Contractor"
        except ObjectDoesNotExist:
            return "Employee"

    def generate_badge(self):
        max_badge = Person.objects.all().aggregate(Max('badge_number'))['badge_number__max']
        if not max_badge:
            max_badge = 11000
        badge = max_badge + 1
        self.badge_number = badge
        self.save()
        return self.badge_number


class Employee(Person):
    employee_id = models.CharField(max_length=7, blank=True)
    visions_id = models.IntegerField(null=True, blank=True)
    sub_type = models.CharField(max_length=1, blank=True)
    marked_as_hired = models.DateField(null=True, blank=True)
    epar_id = models.IntegerField(null=True, blank=True)


class Contractor(Person):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)


class HireDateRange(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


# Service Classes

class Service(models.Model):
    TYPES = (
        ("visions", "Visions"),
        ("synergy", "Synergy"),
        ("ad", "Active Directory"),
        ("cell", "Cell Phone"),
        ("phone", "Desk Phone")
    )
    type = models.CharField(max_length=16, choices=TYPES)
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="services",
    )
    user_info = models.CharField(max_length=50)

    # There can be only one service of each type per Person
    class Meta:
        unique_together = ("type", "person")

    def __unicode__(self):
        return '%s: %s' % (self.type, self.user_data)


# Organizational Classes

class Location(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    location_number = models.CharField(max_length=3)


class Department(models.Model):
    name = models.CharField(max_length=255)
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE)


# Position Classes

class PositionType(models.Model):
    position_type_desc = models.CharField(max_length=255)
    position_name = models.CharField(max_length=255)
    classification = models.CharField(max_length=50)
    is_contracted = models.BooleanField()


class Position(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position_type = models.ForeignKey(PositionType, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, blank=True)
    is_primary = models.BooleanField(default=False)
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=255, blank=True)

    def position_exists_for_user(person):
        positions = Position.objects.filter(person__id=person.id)
        if positions.exists():
            return True
        else:
            return False


# Function for updating data. Use this instead of updating objects directly
# in order to potentially capture in a future changelog/audit model.
def update_field(data_object, column, new_value):
    old_value = getattr(data_object, column)
    if new_value != old_value:
        # Save the new value. In the future could also call an
        # audit/changelog log function
        setattr(data_object, column, new_value)
        data_object.save()
