from django_unicorn.components import UnicornView
from items.models import Selected, WishList
class CardView(UnicornView):
    item:{}
    selected_item:Selected = Selected()
    def mount(self):
        self.item = self.component_kwargs.get('item')
    def add_to_cart(self):
        print('saving')
        self.selected_item.buyer = self.request.user
        self.selected_item.item = self.item
        self.selected_item.save()

    def add_wish_list(self):
        print('saving wish list')
        wl = WishList.objects.get(buyer=self.request.user)
        wl.items.add(self.item)
        wl.save()