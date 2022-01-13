from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_too_cart/<str:pk>/', views.cartForm, name='order'),
    path('cart/', views.cart, name='cart'),
    path('delete/<str:pk>/', views.deleteCart, name='delete'),
    path('deleteall/', views.deleteAllCart, name='deleteAll'),
    path('orderinfo/', views.orderInfo, name='orderInfo'),
    path('panel/', views.panel, name='panel')
]