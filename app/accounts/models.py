from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


def user_avatar(instance, filename):
    # Hard logic to create path to saved folder
    return f'user_{instance.id}/{filename}'


class User(AbstractUser):
    USERNAME_FIELD = "email"
    # ^ Specify what value will be used for login
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField('email adress', unique=True)
    avatar = models.FileField(upload_to=user_avatar)
    # ^ Upload to it is setting path to save this files
    # Set it value name a folder or function or..
    # value to path/%Y/%m/%d/ if need save dated folders
