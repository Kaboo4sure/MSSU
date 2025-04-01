from django.urls import path
from .views import my_orders, seller_orders

urlpatterns = [
    path('my-orders/', my_orders, name='my-orders'),
    path('seller-orders/', seller_orders, name='seller-orders'),
]
