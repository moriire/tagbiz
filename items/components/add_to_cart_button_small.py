from django_unicorn.components import UnicornView
from items.models import Selected
class AddToCartButtonSmallView(UnicornView):
    item = Selected()
    selected_item: Selected = Selected()

    def mount(self):
        self.item = self.component_kwargs.get("item")

    def fsave(self):
        print('saving')
        #self.selected_item.save()
