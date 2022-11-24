from django.contrib import admin
from products.models import Product, Status, Category, Purchase


class PurchaseInline(admin.TabularInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost', 'vendor_cod', 'stock', 'category', 'status')
    list_filter = ('name', 'cost', 'status')
    search_fields = ('name', 'description', 'cost', 'vendor_cod', 'category', 'status')
    inlines = [PurchaseInline]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('availability',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category',)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'order', "cost", 'quantity')
    list_filter = ('user', 'order')
    search_fields = ('user', 'order')

