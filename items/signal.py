from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Item, ItemWithThumbs, Upload, WishList
from users.models import User

@receiver(post_save, sender=User)
def create_item_with_images(sender, created, instance, **kwargs):
    if created:
        WishList.objects.create(
            buyer = instance
        )

@receiver(post_save, sender=Item)
def create_item_with_images(sender, created,instance, **kwargs):
    if created:
        cit = ItemWithThumbs.objects.create(
            item = instance
        )

@receiver(post_save, sender=Upload)
def create_images(sender, created, instance, **kwargs):
    if created:
        iwt_instance = ItemWithThumbs.objects.get(item = instance.item)
        iwt_instance.thumbs.add(instance)
        #.add(instance)