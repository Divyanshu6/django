from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class extendedUser(AbstractUser):
    city=(
      ('Allahabad','Allahabad'),
      ('Patna','Patna'),
      ('Noida','Noida'),
      ('Ajamgadh','Ajamgadh'),
      ('Bhubneshwar','Bhubneshwar'),
    )

    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
)
    age=models.IntegerField(blank=False),
    address=models.CharField(choices=city,max_length=20)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=1)