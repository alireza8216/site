from typing import Text
from django.db import models

from django.utils import timezone

# Create your models here.
class products(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=3000,null=True,blank=True)
    Text = models.TextField(max_length=400000,null=True,blank=True)
    date = models.DateField(default=timezone.now)
    image1 = models.ImageField(upload_to = 'medi/products pics',null=True,blank=True)
    image2 = models.ImageField(upload_to = 'media/products pics',null=True,blank=True)
    image3 = models.ImageField(upload_to = 'media/products pics',null=True,blank=True)
    category1 = models.CharField(max_length=3000,null=True,blank=True)
    category2 = models.CharField(max_length=3000,null=True,blank=True)

    def __str__(self):
        return self.title