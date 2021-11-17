from django.urls import path
from .views import detail,blog

urlpatterns = [
    path('',detail,name='detail'),
    path('<int:num>',blog,name='blog'),
]