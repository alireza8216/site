from django.contrib import admin
from .models import massage
# Register your models here.


class massage_admin(admin.ModelAdmin):
    list_display = ('name', 'text')
    list_filter = ('name', 'date')
    search_fields = ('name', 'text')


admin.site.register(massage, massage_admin)
