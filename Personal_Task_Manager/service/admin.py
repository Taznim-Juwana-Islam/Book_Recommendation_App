from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('Book_title','Book_description','date','status','Book_image')
admin.site.register(Service,ServiceAdmin)
# Register your models here.
