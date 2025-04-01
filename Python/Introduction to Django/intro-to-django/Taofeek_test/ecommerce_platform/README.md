
# E-Commerce Platform Documentation

## Overview
This document provides a comprehensive guide to building a Django-based E-Commerce Platform with support for sellers, buyers, and an admin interface.

## Step-by-Step Setup

### 1. Project Initialization
- Create virtual environment
- Install Django
- Start project: `django-admin startproject ecommerce_platform`
- Create apps: `users`, `products`, `orders`, `dashboard`

### 2. User Authentication
- Define `CustomUser` with `role` field
- Update `AUTH_USER_MODEL` in `settings.py`
- Create registration, login, logout templates and views

### 3. Product Management
- Define `Product` model linked to seller
- Create views for listing, adding, editing, deleting products
- Templates: `product_form.html`, `products_list.html`, `seller_products.html`

### 4. Cart System
- Use session to manage cart
- Views: `add_to_cart`, `remove_from_cart`, `view_cart`
- Template: `cart.html`

### 5. Order Management
- `Order` model with buyer, product, quantity, status
- Views: `checkout`, `my_orders`, `seller_orders`
- Templates: `checkout.html`, `my_orders.html`, `seller_orders.html`

### 6. Dashboard
- Separate app for seller dashboard
- `dashboard_home` view restricted to sellers
- Template: `dashboard_home.html`

### 7. Templates & Routing
- Central `templates/` folder registered in `TEMPLATES` DIRS
- Each app has its own templates folder for modularity
- URLs connected via `include()` in `ecommerce_platform/urls.py`

### 8. Admin Setup
- Register models in `admin.py`
- Create superuser

### Sample Snippet
**Project-level `urls.py`**
```python
path('products/', include('products.urls')),
path('orders/', include('orders.urls')),
path('dashboard/', include('dashboard.urls')),
path('accounts/', include('users.urls')),
```

## Conclusion
This setup supports a full-featured e-commerce flow including user roles, cart, orders, and dashboards.