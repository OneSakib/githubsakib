from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    mob_no = models.IntegerField()
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100)
