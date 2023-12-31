
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("unicorn/", include('django_unicorn.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('shop/', TemplateView.as_view(template_name='shop.html')),
    path('product/<int:pk>/', TemplateView.as_view(template_name='product.html')),
    path('carts/', TemplateView.as_view(template_name='cart.html')),
    path('wish-list/', TemplateView.as_view(template_name='wishlist.html')),
    path('view-cart/', TemplateView.as_view(template_name='wishlist.html')),
    path('checkout/', TemplateView.as_view(template_name='shop-checkout.html')),
    path("auth/", include('users.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)