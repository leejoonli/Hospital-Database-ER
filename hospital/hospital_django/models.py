from django.db import models

# Create your models here.
class Procedure(models.Model):
    name = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.TextField()
    brand = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class Physician(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    ssn = models.IntegerField()

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    registered = models.BooleanField(default=True)
    ssn = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    insurance_id = models.TextField()
    ssn = models.IntegerField()
    pcp = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name