from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self) -> str:
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.date)


class Company(models.Model):
    name = models.CharField(max_length=264, unique=True)
    number_of_employees = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    employee_name = models.CharField(max_length=264, unique=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.employee_name


class Project(models.Model):
    project_name = models.CharField(max_length=264, unique=True)
    employee_name = models.ManyToManyField('Employee')
    team_lead = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='team_lead')

    def __str__(self) -> str:
        return self.project_name
