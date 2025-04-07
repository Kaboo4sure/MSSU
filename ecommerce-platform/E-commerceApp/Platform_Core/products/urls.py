from django.urls import path
from .views import (
    product_list,
    seller_products,
    add_product,
    edit_product,
    delete_product,
    add_to_cart, 
    view_cart,
    remove_from_cart,
    checkout,
)

urlpatterns = [
    path('', product_list, name='product-list'),
    path('seller/', seller_products, name='seller-products'),
    path('seller/add/', add_product, name='add-product'),
    path('seller/edit/<int:pk>/', edit_product, name='edit-product'),
    path('seller/delete/<int:pk>/', delete_product, name='delete-product'),
    path('cart/', view_cart, name='view-cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('checkout/', checkout, name='checkout'),

]
