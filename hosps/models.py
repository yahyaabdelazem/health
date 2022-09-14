from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    beds = models.IntegerField(default=0)
    doctors = models.IntegerField(default=0)
    nurses = models.IntegerField(default=0)
    employees = models.IntegerField(default=0)
    icus = models.IntegerField(default=0)
    incubators = models.IntegerField(default=0)
    hosp_type = models.ForeignKey("HospType", blank=True, null=True, on_delete=models.SET_NULL, related_name='hosptype')
    government = models.ForeignKey("Government", blank=True, null=True, on_delete=models.SET_NULL, related_name='gover')
    admin = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class HospType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HospDept(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Government(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Surgery(models.Model):
    date = models.DateTimeField()
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, related_name='hosp')
    hosp_dept = models.ForeignKey("HospDept", blank=True, null=True, on_delete=models.SET_NULL, related_name='hospdep')
    surg_type = models.ForeignKey("SurgType", blank=True, null=True, on_delete=models.SET_NULL, related_name='hosptyp')

    def __str__(self):
        return self.hospital.name


class SurgType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Report(models.Model):
    date = models.DateField()
    empty_beds = models.IntegerField(default=0)
    empty_icus = models.IntegerField(default=0)
    empty_incubators = models.IntegerField(default=0)
    absent_doctors = models.IntegerField(default=0)
    absent_nurses = models.IntegerField(default=0)
    absent_admins = models.IntegerField(default=0)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, related_name='hosp1')

    def __str__(self):
        return str(self.date)


class Malfunction(models.Model):
    name = models.CharField(max_length=100)
    serial = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    procedure = models.CharField(max_length=200)
    finished = models.BooleanField()
    finished_date = models.DateField()
    report = models.ForeignKey("Report", on_delete=models.CASCADE, related_name='repo')

    def __str__(self):
        return str(self.name)


class Missing(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    procedure = models.CharField(max_length=200)
    finished = models.BooleanField()
    finished_date = models.DateField()
    report = models.ForeignKey("Report", on_delete=models.CASCADE, related_name='repo1')

    def __str__(self):
        return str(self.item)

