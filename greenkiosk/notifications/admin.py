from django.contrib import admin
from .models import Notifications
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user_id","message","time_stamp")
admin.site.register(Notifications,NotificationAdmin)