from re import T
from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False, blank=False, default = 'admin')
    contact = models.CharField(max_length=15, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, null=True)
    father = models.CharField(max_length=40, null=True)
    city = models.CharField(max_length=20, default='Lucknow')

    def __str__(self):
        return self.name

class Subject(models.Model):
    id: models.BigAutoField(primary_key=True)
    code: models.CharField(max_length=10, null=False, default='MATH101')
    name: models.CharField(max_length=20, null=False, default='Mathematics')
    description: models.CharField(max_length=100, null=True)
    instructor: models.CharField(max_length=40, null=True)

class Mark(models.Model):
    id: models.BigAutoField(primary_key=True)
    student: models.ForeignKey(Student, on_delete=models.CASCADE)
    subject: models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks: models.IntegerField(null=True)
