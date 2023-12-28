from django_unicorn.components import UnicornView
from items.models import Category
class FeaturedCategoriesView(UnicornView):
    categories:[Category] = Category.objects.none()
    def  mount(self):
        self.categories = Category.objects.filter(feature=True)