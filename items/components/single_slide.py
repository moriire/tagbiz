from django_unicorn.components import UnicornView

class SingleSlideView(UnicornView):
    item = None
    def mount(self):
        self.item = self.component_kwargs.get('item')