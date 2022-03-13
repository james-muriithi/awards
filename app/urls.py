from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project/<slug>', views.single_project, name="single_project"),
    path('profile', views.profile, name="profile"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('api/projects', views.ProjectsList.as_view()),
    path('api/users', views.ProfilesList.as_view())
]