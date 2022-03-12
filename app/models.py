from django.db import models
# from django.contrib.auth.models import User
from django.utils.text import slugify
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

    def update_user(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()


# project models
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True, unique=True)
    description = models.TextField()
    image = CloudinaryField("image")
    url = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Nairobi")
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_slug(cls, slug):
        project = cls.objects.get(slug=slug)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    # update project
    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.slug = slugify(self.title)
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title
