from django.db import models

# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    yob = models.DateField()

    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    datetime = models.DateTimeField(default="2024-01-01 00:00:00")
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name