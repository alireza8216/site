from django.db import models
from django.utils import timezone


# Create your models here
class article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=2000,null=True,blank=True)
    date = models.DateField(auto_created=timezone.now(),default=timezone.now())
    category1 = models.CharField(max_length=2000,null=True,blank=True)
    category2 = models.CharField(max_length=2000,null=True,blank=True)
    category3 = models.CharField(max_length=2000,null=True,blank=True)
    image = models.ImageField(upload_to='media/article_photos')
    intro = models.TextField(max_length=300000,null=True,blank=True)
    bold_text = models.TextField(max_length=300000,null=True,blank=True)
    text = models.TextField(max_length=300000,null=True,blank=True)
    def __str__(self):
        return self.title

class coment(models.Model):
    article_comment = models.ForeignKey(article,on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)
    email = models.EmailField(max_length=30000)
    website = models.URLField(max_length=3000,null=True,blank=True)
    text = models.TextField(max_length=40000)
    active = models.BooleanField(default=False)
    date =models.DateField(auto_created=timezone.now(),default=timezone.now())