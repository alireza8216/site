from django.shortcuts import render,get_object_or_404
from .models import products
# Create your views here.
def prodacts(request):
    all_products = products.objects.all()
    context = {
        'all_prodacts':all_products,
    }
    return render(request,'portfolio.html',context)

def prodact(request,p_id):
    single_product = get_object_or_404(products,pk=p_id)
    context = {
        'single_product':single_product,
    }
    return render(request,'portfolio-single.html',context)