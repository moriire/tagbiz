from django_unicorn.components import UnicornView

from items.models import Selected

class CartItemsView(UnicornView):
    selections: Selected = Selected.objects.none()
    to_be_added = Selected()
    def mount(self):
        self.selections = Selected.objects.filter(buyer=self.request.user)
