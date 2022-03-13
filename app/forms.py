from django import forms
from django_registration.forms import RegistrationForm

from .models import Project, User


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ('username','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'bio')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'url', 'location')