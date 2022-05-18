from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required

from . models import Category, Product

@login_required
def index(request):
    categories = Category.objects.filter(status=1)
    return render(request, "ness/category.html", {"categories":categories})

def procat(request, slug):
    products = Product.objects.filter(category__slug = slug) 
    return render(request, "ness/products.html", {"products":products})

def single(request, category, slug):
    try:
        product = Product.objects.get(
                category__slug=category, 
                slug = slug)
    except Product.DoesNotExist:
        product = None
    return render(request, "ness/single.html", {"product":product})


class Cart:
    def __init__(self, request, pid):
        self.pid = pid
        self.cart = {}
        request.session["cart"] = self.cart
        self.sess = request.session["cart"]
    def __iter__(self):
        return self.sess.get("cart")

    def add(self):
        if self.pid in self.sess:
            self.sess[self.pid] += 1
        else:
            self.sess[self.pid] = 1
        return self.sess

    def remove(self):
        try:
            del self.sess
        except KeyError:
            pass
        finally:
            return "deleted..."


#@login_required
def addtocart(request, pid):
    cart = Cart(request, pid=pid)
    return HttpResponse("ghhhhj")#cart.add())

#@login_required
def removeFromCart(request, pid):
    cart = Cart(pid=pid)
    return HttpResponse("deleted.")


