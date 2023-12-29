from django_unicorn.components import UnicornView

class SingleSlideView(UnicornView):
    item = None
    user = None
    def mount(self):
        self.user = self.request.user
        self.item = self.component_kwargs.get('item')

    def add_to_cart(self):
        print('saving')
        self.parent.parent.add_to_cart(self.item)
        