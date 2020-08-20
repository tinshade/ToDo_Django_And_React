from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, BlukUploadSerializer
from .models import Task,BulkUpload, AutoData
import os
from tablib import Dataset
from .resources import AutoDataResource
from django.http import JsonResponse
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
    stuff = Task.objects.all()
    data = AutoData.objects.all()
    return render(request, 'main/index.html', {'title':'ToDo Display', 'items': stuff, 'data': data})





## Rest of the CRUD ##


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'BulkUpload':'/task-bulk/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks  = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks  = Task.objects.get(id= pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

### Excel Read And Import ###
@api_view(['POST'])
def taskBulk(request):
    serializer = BlukUploadSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
##Buddy View##
def parse_upload(request):
    data_store = AutoDataResource()
    dataset = Dataset()
    #data_file = open(os.path.join(BASE_DIR, b.bulkfile.url),"r")
    data_file = BulkUpload.objects.all().order_by('-id')[0].bulkfile
    imported_data = dataset.load(data_file.read())
    result = data_store.import_data(dataset, dry_run=False)
    return JsonResponse({"r": "Done"}, safe=False)





@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,  data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("I got rid of that for you!")