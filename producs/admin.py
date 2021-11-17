from django.contrib import admin
from .models import products

# Register your models here.
class product_admin(admin.ModelAdmin):
    list_display = ('title','date','category1')
    list_filter = ('title','date')
    search_fields = ('title','text')

admin.site.register(products,product_admin)