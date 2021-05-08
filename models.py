from django.db import models

class Student(models.Model):
    std_id = models.IntegerField(max_length=10, null=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=20, null=True)
