from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    


class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_photos/')

    # def __str__(self):
    #     return self.username
