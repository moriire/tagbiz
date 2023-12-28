from django_unicorn.components import UnicornView
from items.models import Item
class ProductsListView(UnicornView):
    items: Item = Item.objects.none()
    no_of_items:int = 0
    def mount(self):
        self.items = Item.objects.all()#filter(promo='banner')
        self.no_of_items = len(self.items)