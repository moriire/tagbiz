from django_unicorn.components import UnicornView


class CardView(UnicornView):
    item:{}
    def mount(self):
        self.item = self.component_kwargs.get('item')
