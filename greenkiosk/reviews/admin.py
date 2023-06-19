from django.contrib import admin
from .models import Reviews
# Register your models here.

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("user_id","product_id","ratings","comments")
admin.site.register(Reviews,ReviewsAdmin)