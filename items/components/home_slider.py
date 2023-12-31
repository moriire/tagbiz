from django_unicorn.components import UnicornView
from items.models import ItemWithThumbs
class HomeSliderView(UnicornView):
    items:ItemWithThumbs = ItemWithThumbs.objects.select_related('item').prefetch_related('thumbs').none()
    def mount(self):
        self.items = ItemWithThumbs.objects.select_related('item').all().prefetch_related('thumbs')