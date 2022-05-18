from django.contrib import admin

from .models import Product, Category, Payment, Order, OrderItem, Address

from django.conf import settings

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}

class CategoryAdmin(admin.ModelAdmin):              prepopulated_fields = {"slug": ('title', )}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
#admin.site.register(Category)
