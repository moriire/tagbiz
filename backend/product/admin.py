from django.contrib import admin
from .models import Product
from thumbs.models import ProductImage
from django.utils.html import format_html


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('img', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="100" height="100" />', obj.img.url)
        return "No Image"

    image_preview.short_description = "Image Preview"

class ProductAdmin(admin.ModelAdmin):
      inlines = (ProductImageInLine,)
      list_display = ("image_preview", "name", "price", "discount", "discounted_price", "new_price", )
      ordering = ('-created_at',)
      search_fields = ('name',)

      def image_preview(self, obj):
        images = obj.images.all()
        return format_html("".join([
            f'<img src="{image.img.url}" style="width: 50px; height: auto; margin-right: 5px;" />'
            for image in images
        ]))

      image_preview.short_description = "Image Preview"
      
admin.site.register(Product, ProductAdmin)