from django_unicorn.components import UnicornView
from items.models import ItemWithThumbs
class PopularProductsView(UnicornView):
    items: ItemWithThumbs = ItemWithThumbs.objects.none()
    no_of_items:int = 0
    def mount(self):
        self.items = ItemWithThumbs.objects.filter(item__promo='popular')
        self.no_of_items = len(self.items)
