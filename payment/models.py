from django.db import models

# Create your models here.
class vid(models.Model):
    name = models.CharField(max_length=50)
    path = models.FileField(upload_to='media/videos/')
    