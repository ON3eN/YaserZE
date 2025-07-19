from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'order_date', 'is_paid']
    search_fields = ['customer_name']
    list_filter = ['is_paid', 'order_date']
