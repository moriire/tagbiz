from django_unicorn.components import UnicornView, QuerySetType
from django_unicorn.components import UnicornView, QuerySetType
from items.models import Selected, WishList, ItemWithThumbs, Category
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseView(LoginRequiredMixin, UnicornView):
    categories:QuerySetType[Category] = Category.objects.none()
    popular_items: QuerySetType[ItemWithThumbs] =  ItemWithThumbs.objects.none
    selections: QuerySetType[Selected] = []
    wishlists:QuerySetType[WishList] = []
    featured_categories = []
    selected_item = Selected()
    cart_count:int = 0
    wish_count:int = 0
    user = None
    def all_items(self):
        return ItemWithThumbs.objects.all()
    
    def cats(self):
        return Category.objects.all()
    
    def wish_lists(self):
        return WishList.objects.all()
    
    def mount(self):
        self.user = self.request.user
        self.featured_cats()
        self.update()
        print("pkay ooooo", self.request.user)

    def update(self):
        self.update_selection()
        self.update_wishlist()
        self.popular_items = self.all_items().filter(item__promo='popular')
    
    def update_selection(self):
        self.selections = Selected.objects.all().filter(buyer=self.user)# if self.request.user.is_authenticated else []
        self.cart_count = len(self.selections)

    def update_wishlist(self):
        wishes = WishList.objects.get(buyer=self.user)# if self.request.user.is_authenticated else {}
        self.wishlists = wishes.items.all()
        self.wish_count = len(self.wishlists)

    def featured_cats(self):
        self.cats()
        self.featured_categories = self.cats().filter(feature=True)

    def add_to_cart(self, item):
        print('saving')
        self.selected_item.buyer = self.user
        self.selected_item.item = item
        self.selected_item.save()
        
    def add_wish_list(self, item:ItemWithThumbs):
        print('saving wish list')
        wl = WishList.objects.get(buyer=self.user)
        wl.items.add(item)
        wl.save()
        