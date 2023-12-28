from django_unicorn.components import UnicornView

class AddToCartButtonBigView(UnicornView):
    def mount(self):
        print('hello')

    def save(self):
        print('yes')
