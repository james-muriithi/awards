from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Project, User
from app.serializer import ProjectsSerializer, UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')


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