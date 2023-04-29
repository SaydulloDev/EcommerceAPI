from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    age = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.first_name
