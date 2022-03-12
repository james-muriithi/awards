from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/projects', views.ProjectsList.as_view()),
    path('api/users', views.ProfilesList.as_view())
]