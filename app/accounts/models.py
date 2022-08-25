from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = "email"
    # ^ Specify what value will be used for login
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField('email adress', unique=True)
