from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url = True)
    xlfile = serializers.FileField(max_length=None, use_url = True)
    class Meta:
        model = Task
        fields = '__all__'