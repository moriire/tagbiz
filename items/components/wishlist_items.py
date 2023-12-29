from django_unicorn.components import UnicornView, QuerySetType
from items.models import WishList
class WishlistItemsView(UnicornView):
    wishes = []#WishList.objects.none()
    #to_be_added = WishList()
    def mount(self):
        wl = WishList.objects.get(buyer=self.request.user) if self.request.user.is_authenticated else None
        print(wl)
        self.wishes = wl.items.all()