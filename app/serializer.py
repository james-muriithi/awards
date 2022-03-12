from rest_framework import serializers
from .models import Project, Rating, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class ProjectsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()

    class Meta:
        model = Project
        fields = '__all__'


class RatingsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectsSerializer(read_only=True)
    user_id = serializers.IntegerField()
    project_id = serializers.IntegerField()

    class Meta:
        model = Rating
        fields = '__all__'
