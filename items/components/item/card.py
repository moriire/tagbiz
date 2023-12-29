from django_unicorn.components import UnicornView, QuerySetType
class CardView(UnicornView):
    item: {}

    def mount(self):
        self.item = self.component_kwargs.get('item')
        
    def add_to_cart(self):
        self.parent.parent.add_to_cart(self.item)
    def add_wish_list(self):
        print('saving wish list')
        self.parent.parent.add_wish_list(self.item)