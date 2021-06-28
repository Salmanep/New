from django.db import models
class Hospital(models.Model):
    district = models.CharField(max_length=30)
    hospital = models.CharField(max_length=100, primary_key=True)
    photo = models.FileField()
    details = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    emergency = models.CharField(max_length=300)
class Doctors(models.Model):
    district = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    doctor = models.CharField(max_length=50, primary_key=True)
    photo = models.FileField()
    details = models.CharField(max_length=300)
class Sikk(models.Model):
    disease = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=1000)
    cause = models.CharField(max_length=500)
    department = models.CharField(max_length=50)
    symptom1 = models.CharField(max_length=300)
    symptom2 = models.CharField(max_length=300)
    symptom3 = models.CharField(max_length=300)
    symptom4 = models.CharField(max_length=300)
class User(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name =models.CharField(max_length=50)
    Email = models.EmailField()
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

