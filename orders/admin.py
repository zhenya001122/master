from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "address", 'date', "status")
    list_filter = ('user', 'date', 'status')
    search_fields = ('user', 'date', 'status')
