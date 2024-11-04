from django.db import models
from utils import  image_resize
import uuid
from product.models import Product
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

def product_image_path(instance, filename):
    return '/'.join([str(instance.product.id), filename])

class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    img = models.ImageField(_("Upload Image"), upload_to=product_image_path,)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    def get_image(self):
        return self.img.url
    
    def save(self, *args, **kwargs):
        if self.img.file:
            image_resize(self.img, 500, 600)
        super().save(*args, **kwargs)