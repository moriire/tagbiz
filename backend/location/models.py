from django.db import models
class Location(models.Model):
    region = models.CharField(max_length=40)
    cost = models.FloatField()

    def __str__(self):
        return self.region