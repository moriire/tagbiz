from django_unicorn.components import UnicornView

class HeaderView(UnicornView):
    selections = []
    wishlists = []
    cart_count = 0
    wish_count = 0
    categories = []

    def mount(self):
        self.categories = self.parent.categories #self.component_kwargs.get('categories')
        self.selections = self.parent.selections#.component_kwargs.get('selections')
        self.wishlists = self.parent.wishlists#component_kwargs.get('wishlists')
        self.cart_count = self.parent.cart_count #self.component_kwargs.get('cart_count')
        self.wish_count = self.parent.wish_count #component_kwargs.get('wish_count')
