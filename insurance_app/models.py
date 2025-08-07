from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('customer', 'Customer'),
        ('doctor', 'Doctor')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

class InsurancePlan(models.Model):
    name = models.CharField(max_length=255)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage = models.TextField()

class UserPolicy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(InsurancePlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Claim(models.Model):
    policy = models.ForeignKey(UserPolicy, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')


# Create your models here.
