from django_unicorn.components import UnicornView
from items.models import Category
class CategoriesSidebarView(UnicornView):
    categories:[Category] = []
    def  mount(self):
        self.categories = Category.objects.all()