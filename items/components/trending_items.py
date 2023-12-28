from django_unicorn.components import UnicornView
from items.models import Item

class TrendingItemsView(UnicornView):
    items: Item = Item.objects.none()
    def mount(self):
        self.items = Item.objects.filter(promo='trending')
