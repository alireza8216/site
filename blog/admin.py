from django.contrib import admin
from .models import article , coment


# Register your models here.
class blog_admin(admin.ModelAdmin):
    list_display = ('title','date','category1')
    list_filter = ('title','date')
    search_fields = ('title','text')

admin.site.register(article ,blog_admin)

class comment_admin(admin.ModelAdmin):
    list_display = ('name','active')
    list_filter = ('name',)
    search_fields = ('name','text')
    actions = ['activate']
    def activate (self,request,queryset):
        queryset.update(active=True)
        


admin.site.register(coment ,comment_admin)
