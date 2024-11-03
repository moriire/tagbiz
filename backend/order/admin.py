from django.contrib import admin
from .models import Order
from product.models import Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class OrderAdmin(admin.ModelAdmin):
      #inlines = (ProductInline,)
      list_display = ("created_by", "carts", "mode", "address", "status", "amount")
      ordering = ('-created_on',)
      search_fields = ('craeted_by',)

      @admin.display(description='items')
      def carts(self, obj):
            return [item.name for item in obj.cart.all()]

admin.site.register(Order, OrderAdmin)