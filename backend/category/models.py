from django.db import models
from django.template.defaultfilters import slugify
class ProductCategory(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField(unique=True, editable=False, db_index=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
       
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name =("Category")
        verbose_name_plural = ("Product Categories")