
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = [
    re_path(r'^su/', include('django_su.urls')),
    path("admin/lookups/", include(ajax_select_urls)),
    path('admin/', admin.site.urls),
    path("unicorn/", include('django_unicorn.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('shop/', TemplateView.as_view(template_name='shop.html')),
    path('carts/', TemplateView.as_view(template_name='cart.html')),
    path('wish-list', TemplateView.as_view(template_name='wishlist.html')),
    path("auth", include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
