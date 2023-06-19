from django.contrib import admin
from .models import Ordering
# Register your models here.

class OrderingAdmin(admin.ModelAdmin):
    list_display = ("user_id","products","total_price","shipping_address","order_date")
admin.site.register(Ordering,OrderingAdmin)
