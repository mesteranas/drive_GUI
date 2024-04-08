from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Files(models.Model):
    title=models.CharField(max_length=500)
    file=models.FileField(upload_to="static/files")
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)