from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, blank=False)
    completed = models.BooleanField(default=False, blank=False, null=True)
    image = models.ImageField(upload_to="User_Images/", default="User_Images/no.png")
    xlfile = models.FileField(upload_to="Docs/", default="Docs/no.pdf")
    def __str__(self):
        return self.title

class BulkUpload(models.Model):
    author = models.CharField(max_length=20, default="Abhishek")
    bulkfile = models.FileField(upload_to="Bulk/")
    is_uploaded = models.BooleanField(default=False)
    uploaded_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author

class AutoData(models.Model):
    u_name = models.CharField(max_length=40, blank=False, null=False)
    bio = models.TextField(max_length=200, blank=False, null=False)
    is_active = models.BooleanField(blank=False, null=False, default=False)
    phone = models.IntegerField(blank=False, null=False)
    email_id = models.EmailField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.u_name
