from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Project, User
from app.forms import ProjectForm
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

@login_required()
def single_project(request, slug):
    project = Project.get_project_by_slug(slug)
    return render(request, 'single-project.html', {'project': project})



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