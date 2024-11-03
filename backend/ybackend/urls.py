from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from product.views import ProductView
from location.views import LocationView
from category.views import ProductCategoryView
from thumbs.views import ProductImageView
from order.views import OrderView
from rest_framework.routers import  DefaultRouter

admin.site.site_header = 'Tagbiz Admin'
admin.site.site_title = "Tagbiz"
admin.site.index_title = "Tagbiz Site administration"
admin.site.site_url = "/"

router = DefaultRouter()
router.register("products", ProductView)
router.register("categories", ProductCategoryView)
router.register("locations", LocationView)
router.register("upload", ProductImageView)
router.register("orders", OrderView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)