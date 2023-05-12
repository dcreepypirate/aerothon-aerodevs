from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

    

class User(AbstractUser):
    LOGIN_TYPE = [
        ("R", "Recycler"),
        ("M", "Manufacturer"),
        ("A", "Airline"),
    ]
    role = models.CharField(max_length=1,choices = LOGIN_TYPE,null=True)
