from django_unicorn.components import UnicornView

class HeaderTwoView(UnicornView):
    selections = []
    wishlists = []
    cart_count = 0
    wish_count = 0

    def mount(self):
        self.update_header()

    def update_header(self):
        self.parent.update_selection()
        self.parent.update_wishlist()
        self.selections = self.parent.selections
        self.wishlists = self.parent.wishlists
        self.cart_count = self.parent.cart_count
        self.wish_count = self.parent.wish_count
