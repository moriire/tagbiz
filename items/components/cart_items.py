from django_unicorn.components import UnicornView
from items.models import Selected

class CartItemsView(UnicornView):
    cart_count = 0
    def mount(self):
        self.cart_count = len(self.parent.selections)
