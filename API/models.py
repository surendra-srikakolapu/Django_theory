from django.db import models


# Create your models here.


class Employee(models.Model):

    name = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")
