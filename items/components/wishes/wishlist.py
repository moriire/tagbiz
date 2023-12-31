from django_unicorn.components import UnicornView, QuerySetType
from items.models import Selected, WishList, ItemWithThumbs, Category
from django.contrib.auth.mixins import LoginRequiredMixin

class WishlistView(LoginRequiredMixin, UnicornView):
    pass