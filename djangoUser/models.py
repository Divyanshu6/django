from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class extendedUser(AbstractUser):
    age=models.IntegerField(blank=False),
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=1)

    def __str__(self):
      return self.first_name