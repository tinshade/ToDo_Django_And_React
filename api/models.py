from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, blank=False)
    completed = models.BooleanField(default=False, blank=False, null=True)
    image = models.ImageField(upload_to="User_Images/", default="User_Images/no.png")
    xlfile = models.FileField(upload_to="Docs/", default="Docs/no.pdf")
    def __str__(self):
        return self.title