from django.urls import path

from ness import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:slug>', views.procat, name='category'),
    path('<str:category>/<str:slug>', views.single, name='single-product'),
    path('add/<int:pid>/', views.addtocart, name='add-product'),
    path('<int:pid>/remove', views.removeFromCart, name='rem-product'),
]
