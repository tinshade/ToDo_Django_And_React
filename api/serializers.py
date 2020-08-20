from rest_framework import serializers
from .models import Task, BulkUpload

class TaskSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url = True)
    xlfile = serializers.FileField(max_length=None, use_url = True)
    class Meta:
        model = Task
        fields = '__all__'


class BlukUploadSerializer(serializers.ModelSerializer):
    bulkfile = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = BulkUpload
        fields = "__all__"