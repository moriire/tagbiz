from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from product.views import ProductView
from thumbs.views import ProductImageView
from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=True)
router.register("products", ProductView)
router.register("upload", ProductImageView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)