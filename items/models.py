from collections.abc import Iterable
from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image
from django.contrib.auth.backends import UserModel
User = UserModel()

class Category(models.Model):
    name = models.CharField(max_length=15)
    feature = models.BooleanField(default=False)
    def __unicode__(self) -> str:
        return self.name
  
class Item(models.Model):
    class Promo(models.TextChoices):
        basic = 'basic'
        banner = 'banner'
        trending = 'trending'
        popular = 'popular'
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.CharField(max_length=30)#ForeignKey(Crop, related_name="crop_produce", on_delete=models.CASCADE)
    price = models.FloatField()
    ptg_discount = models.FloatField(default = 0.0)
    sold = models.IntegerField(default=0)
    stock = models.IntegerField(default=1)
    promo = models.CharField(max_length=20, choices = Promo.choices)
    desc = models.TextField(default="")
    
    def __str__(self) -> str:
        return self.item
    
    def new_price(self):
        return (1-(0.01*self.ptg_discount))*self.price

class Upload(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='upload_item')
    img = models.ImageField(blank=True, null=True, upload_to='images/')
    
class ItemWithThumbs(models.Model):
    item = models.ForeignKey(Item, related_name="item_with_thumbs", on_delete=models.CASCADE)
    thumbs = models.ManyToManyField(Upload, related_name='item_images', blank=True)

class Selected(models.Model):
    item = models.ForeignKey(ItemWithThumbs, related_name="selected_item", on_delete=models.CASCADE)
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="selected_item_buyer")
    unit = models.IntegerField(default=1)
    noted = models.BooleanField(default=False)
    def __unicode__(self) -> str:
        return self.item
    
    def cart_item_amount(self):
        return self.item.price * self.unit

class WishList(models.Model):
    items = models.ManyToManyField(ItemWithThumbs, related_name="wishlist_item")
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_item")
    def __unicode__(self) -> str:
        return self.buyer