import email
from django.shortcuts import render

from contact.models import massage
from .forms import masseg_form
# Create your views here.
from django.core import mail
from django.conf import settings

def send(request):
    new_masseg = None
    if request.method == "POST":
        massegform = masseg_form(request.POST, request.FILES)
        if massegform.is_valid():
            new_comment = massegform.save(commit=False)
            new_comment.save()
    else:
        massegform= masseg_form()
    
    contex = {
        'new_masseg':new_masseg,
        'messageform':massegform
    }
    return render(request,'contact.html',contex)
    
def messages(request):
    all_massages = massage.objects.all()
    contex = {
        'all_message':all_massages,
    }
    return render(request,'contac.html',contex)    