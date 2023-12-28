from django_unicorn.components import UnicornView
from items.models import ItemWithThumbs

class TrendingItemsView(UnicornView):
    items: ItemWithThumbs = ItemWithThumbs.objects.none()
    def mount(self):
        self.items = ItemWithThumbs.objects.filter(item__promo='trending').select_related('item').prefetch_related('thumbs')
