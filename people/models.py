from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    address = models.TextField(blank=True)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)


class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)

class Employee(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250, null=True)
    joining_date = models.DateField()
    referred_by = models.ForeignKey("Employee", null=True,on_delete=None)
    experience = models.FloatField(default=0)
    photo_url = models.CharField(max_length=500, null=True)
    status = models.BooleanField(default=True)
    dob = models.DateField()
    contact = models.OneToOneField(ContactDetails,on_delete=None, null=True)
    sex = models.CharField(max_length=2, default='M')

class EmployeeTeams(models.Model):
    employee = models.ForeignKey(Employee, on_delete=None)
    team = models.ForeignKey(Team, on_delete=None)

class EmployeeProduct(models.Model):
    employee = models.ForeignKey(Employee,on_delete=None)
    project = models.ForeignKey(Product, on_delete=None)


