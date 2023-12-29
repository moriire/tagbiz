from django_unicorn.components import UnicornView

class HeaderTwoView(UnicornView):
    selections = []
    cart_count = 0

    def mount(self):
        self.selections = self.parent.selections
        self.cart_count = self.parent.cart_count
