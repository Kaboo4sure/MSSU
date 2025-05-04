from django.urls import path, include
from .views import my_orders, seller_orders, update_profile

urlpatterns = [
    path('my-orders/', my_orders, name='my-orders'),
    path('seller-orders/', seller_orders, name='seller-orders'),
    path('profile/', update_profile, name='profile'),
]
