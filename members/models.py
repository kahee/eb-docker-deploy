from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(blank=True, max_length=100)
    img_profile = models.ImageField(upload_to='user', blank=True)
