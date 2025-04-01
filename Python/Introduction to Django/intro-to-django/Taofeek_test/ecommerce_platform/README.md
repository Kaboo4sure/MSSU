
# E-Commerce Platform Setup Guide
**Generated on:** 2025-04-01 07:50:36

## 1. Project Overview
This Django-based e-commerce platform supports buyer, seller, and admin roles. Features include user authentication, product listings, shopping cart, and order management.

## 2. Folder Structure
```
ecommerce_platform/
├── dashboard/
├── orders/
├── products/
├── users/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── products_list.html
│   ├── cart.html
│   └── dashboard/dashboard_home.html
```

## 3. Key Features
- Role-based authentication
- Product creation, editing, and deletion by sellers
- Buyers can add to cart, view cart, and place orders
- Seller dashboard for order and product management

## 4. Important URLs
```
/ -> Home Page
/products/ -> Product Listings
/products/seller/ -> Seller Product Management
/products/seller/add/ -> Add Product
/cart/ -> View Shopping Cart
/orders/checkout/ -> Checkout Page
/orders/my-orders/ -> Buyer Orders Page
/orders/seller-orders/ -> Seller Orders Page
/dashboard/ -> Seller Dashboard
/admin/ -> Admin Panel
```

## 5. Notes
Make sure all templates are placed correctly and settings.py has 'templates' directory registered in TEMPLATES > DIRS.
