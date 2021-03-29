from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username
