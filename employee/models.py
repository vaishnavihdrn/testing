from django.db import models
from datetime import date, datetime

# Create your models here.
class Role(models.Model):
    name=models.CharField(max_length=50)
    desc = models.TextField(default='')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    doj=models.DateField(default=date.today)
    active=models.BooleanField(default=True)

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day)<(self.dob.month,self.dob.day))

    def experience(self):
        today = date.today()
        return today.year - self.doj.year - ((today.month, today.day) < (self.doj.month, self.doj.day))

    def __str__(self):
        return self.name