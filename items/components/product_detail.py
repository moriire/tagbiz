from django_unicorn.components import UnicornView
from items.models import ItemWithThumbs
class ProductDetailView(UnicornView):
    item = ItemWithThumbs.objects.none()
    images = []

    def mount(self):
        id = self.request.path_info.rstrip('/').split('/')[-1]
        self.item = ItemWithThumbs.objects.get(pk = id)# self.request.GET.get('pk') )
        self.images = self.item.thumbs.all()