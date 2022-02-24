from django.shortcuts import render
from django.http import HttpResponse
from .models import vid
# Create your views here.
def video(request):
    vids =  vid.objects.all()
    con = {
        'vides':vids
    }
    return render(request,'vid.html',con)