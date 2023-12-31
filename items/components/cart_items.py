from django_unicorn.components import UnicornView
from items.models import Selected

class CartItemsView(UnicornView):
    cart_count = 0
    selections = []
    def mount(self):
        self.selections = self.component_kwargs.get('selections')
        self.cart_count = self.component_kwargs.get('cart_count')