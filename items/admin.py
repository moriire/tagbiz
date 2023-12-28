from django.contrib import admin
from .models import Item, Upload, Category, Selected, WishList, ItemWithThumbs
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Upload)
admin.site.register(ItemWithThumbs)
admin.site.register(Selected)
admin.site.register(WishList)