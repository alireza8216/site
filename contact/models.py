from django.db import models
from django.utils import timezone
# Create your models here.
class massage (models.Model):
    name = models.CharField(max_length=20000)
    emale = models.EmailField(max_length=30000)
    subject = models.CharField(max_length=20000)
    text = models.TextField(max_length=500000)
    date = models.DateField(default=timezone.now())
    profile = models.ImageField(upload_to = 'user pics/',null=True,blank=True)