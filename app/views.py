from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
import cloudinary
import cloudinary.uploader
import cloudinary.api

from app.models import Project, Rating, User
from app.forms import ProfileForm, ProjectForm
from app.serializer import ProjectsSerializer, UserSerializer

# Create your views here.


def index(request):
    projects = Project.get_all_projects()
    return render(request, 'index.html', {'projects': projects})


@login_required()
def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect(request.META.get('HTTP_REFERER'), {'success': 'Project Uploaded Successfully'})

    return redirect(request.META.get('HTTP_REFERER'), {'error': 'Project Uploaded Successfully'})


# delete project
@login_required()
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete_project()
    return redirect("/profile", {"success": "Project Deleted Successfully"})

# rate_project


@login_required(login_url="/accounts/login/")
def rate_project(request, id):
    if request.method == "POST":

        project = Project.objects.get(id=id)
        current_user = request.user

        design_rate = request.POST["design"]
        usability_rate = request.POST["usability"]
        content_rate = request.POST["content"]

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
        )

        return redirect("profile", {"success": "Project Rated Successfully"})


@login_required()
def single_project(request, slug):
    project = Project.get_project_by_slug(slug)
    return render(request, 'single-project.html', {'project': project})


@login_required()
def profile(request):
    title = f'Profile {request.user.full_name}'
    return render(request, 'profile.html', {'title': title})


@login_required()
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            request.user.full_name = form.data['full_name']
            request.user.bio = form.data['bio']
            request.user.save()
        return redirect(request.META.get('HTTP_REFERER'), {'success': 'Profile updated successfully'})


@login_required()
def update_avatar(request):
    if request.method == 'POST' and request.FILES['avatar']:
        profile_image = cloudinary.uploader.upload(request.FILES['avatar'])
        request.user.avatar = profile_image['url']
        request.user.save()
        return redirect(request.META.get('HTTP_REFERER'), {'success': 'Profile updated successfully'})


class ProjectsList(APIView):
    def get(self, request):
        projects = Project.get_all_projects()
        serializers = ProjectsSerializer(projects, many=True)

        return Response(serializers.data)


class ProfilesList(APIView):
    def get(self, request):
        users = User.get_all_users()
        serializers = UserSerializer(users, many=True)

        return Response(serializers.data)
