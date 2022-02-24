from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request):
  username = None
 
  if request.user.is_authenticated:
    username = request.user.username
    group = []
    for i in request.user.groups.all():
      group.append(i.name)

    if 'اساتید' in group:

      context = {
        'username':username
      }
      return render(request,'index.html',context)
    else:
      #print(request.user.groups.all())
      #return HttpResponse(' عزیز شما جزو اساتید نیستید{}'.format(username))
      context = {
        'username':username
      }
      return render(request,'index.html',context)
    