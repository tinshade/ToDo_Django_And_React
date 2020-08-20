from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings    

urlpatterns=[
    path('', views.api_overview, name="api-overview"),
    path('show', views.home, name='show'),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-bulk/', views.taskBulk, name="task-bulk"),
    path('parse_upload/', views.parse_upload, name="parse_upload"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)