from django.db import models
from items.models import Selected
from users.models import User

class Cart(models.Model):
    item = models.ManyToManyField(Selected, related_name="add_item", blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    unit = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.user.get_full_name()
    