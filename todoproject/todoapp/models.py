from django.db import models

# Create your models here.
class Todo(models.Model):
    firstname= models.CharField(max_length=255)
    secondname= models.CharField(max_length=255,null=True)
    job = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
class Test(models.Model):
    pass
