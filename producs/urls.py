from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.prodacts,name='all_products'),
    path(r'<int:p_id>',views.prodact,name='single_product'),
]