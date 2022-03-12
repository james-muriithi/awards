from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=124)
    email = models.CharField(max_length=124, unique=True)
    avatar = CloudinaryField('image', null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    @property
    def url_formatted_name(self):
        return self.full_name.replace(' ', '+') or self.username

    @property
    def user_avatar(self):
        return self.avatar if self.avatar else f'https://ui-avatars.com/api/?name={self.url_formatted_name}&background=49c5b6&color=fff'
