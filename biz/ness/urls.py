from django.urls import path
from ness import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:slug>/', views.procat, name='category'),
    path('<str:category>/<str:slug>/', views.single, name='single-product'),
    path('cart/', views.shoppingCart, name='shopping-cart'),
    path('remove/<int:product_id>/', views.removeItem, name='remove-item')
]

