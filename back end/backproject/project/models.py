from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    avatarUrl = models.ImageField()
    usertag = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    birthday = models.DateField()
    phone = models.CharField(max_length=30)