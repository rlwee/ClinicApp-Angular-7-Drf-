from django.db import models
from django.utils import timezone

# Create your models here.


class Clients(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    mothersName = models.CharField(max_length=100)
    fathersName = models.CharField(max_length=100)
    contactNumberM = models.CharField(max_length=100)
    contactNumberF = models.CharField(max_length=100)
    pediaName = models.CharField(max_length=100)
    history = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    payment = models.IntegerField()
    therapyType = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey('Clients', on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    ref = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    paid = models.IntegerField()
    schedule = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return "{} {}".format(self.client, self.schedule)

class Employee(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    SSS = models.CharField(max_length=200)
    TIN = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Workload(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    tasks = models.CharField(max_length=500)

    def __str__(self):
        return self.employee


class Sales(models.Model):
    day = models.IntegerField()
    week = models.IntegerField()
    month = models.IntegerField() 