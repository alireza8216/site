from django.urls import path
from .views import detail,blog, to_json , go_to_gateway_view

urlpatterns = [
    path('',detail,name='detail'),
    path('<int:num>',blog,name='blog'),
    path('jason/',to_json,name='js'),
    path('bank/', go_to_gateway_view , name='bank')
]