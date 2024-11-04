from django.db import models
from rest_framework.serializers import ModelSerializer

class AppModel(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    title = models.CharField(max_length=40, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    hero = models.ImageField(null=True, blank=True)
    description = models.TextField(default="")
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name =("App Data")
        verbose_name_plural = ("Application Information")
        
    def __str__(self):
        return self.name
    
class AppModelSerializer(ModelSerializer):
    class Meta:
        model = AppModel
        fields = "__all__"