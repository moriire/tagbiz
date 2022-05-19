from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.contrib.auth.decorators import login_required



from .cart import Cart

from django.conf import settings

from . models import Category, Product

@login_required(login_url='/auth/login/')
def index(request):
    categories = Category.objects.filter(status=1)
    return render(request, "ness/category.html", {"categories":categories})

def procat(request, slug):
    products = Product.objects.filter(category__slug = slug)
    return render(request, "ness/products.html", {"products":products})

#@login_required
def single(request, category, slug):
    if request.POST:
        cart = Cart(request)
        units = request.POST.get("units")
        amount = request.POST.get("amount")
        product = Product.objects.get(                   slug = slug)
        cart.add(product, quantity=int(units)) 
        return HttpResponse({"a":cart})
    else:
        try:
            product = Product.objects.get(category__slug=category,slug = slug)
        except Product.DoesNotExist:
            product = None
        finally:
            return render(request, "ness/single.html", {"product":product})



@login_required
def shoppingCart(request):
    cart = Cart(request)
    return render(request, "ness/cart.html", {"items": cart})

#@login_required
def removeItem(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id)
    if cart.remove(product):
        return redirect('cart/')
