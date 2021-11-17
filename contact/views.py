from django.shortcuts import render
from .forms import masseg_form
# Create your views here.
from django.core import mail

def send(request):
    new_masseg = None
    if request.method == "POST":
        massegform = masseg_form(data=request.POST)
        if massegform.is_valid():
            new_masseg = massegform.save()
            mail.send_mail(
                'new masseg',
                'you have new massege on website',
                'a8888ralireza@gmail.com',
                ['a8888ralireza@gmail.com'],
                fail_silently=False
            )
    else:
        massegform= masseg_form()

    contex = {
        'new_masseg':new_masseg
    }
    return render(request,'contact.html',contex)
    