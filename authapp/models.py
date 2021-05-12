from django.db import models
from django.contrib.auth.models import AbstractUser


class OnlineShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, blank=True)
