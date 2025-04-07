
# E-Commerce Platform Documentation

## Overview
This document provides a comprehensive guide to building a Django-based E-Commerce Platform with support for sellers, buyers, and an admin interface. It includes user authentication, product listings, shopping cart functionality, order management, and a seller dashboard — all styled with custom CSS.

## Step-by-Step Setup

### 1. Project Initialization
- Create a virtual environment:  
  ```bash
  python -m venv env
  source env/bin/activate  # or `env\Scripts\activate` on Windows
  ```
- Install Django:  
  ```bash
  pip install django
  ```
- Start project and apps:  
  ```bash
  django-admin startproject ecommerce_platform
  cd ecommerce_platform
  python manage.py startapp users
  python manage.py startapp products
  python manage.py startapp orders
  python manage.py startapp dashboard
  ```

### 2. User Authentication
- Create a `CustomUser` model in `users/models.py` with a `role` field (e.g., `buyer`, `seller`)
- Update `settings.py`:  
  ```python
  AUTH_USER_MODEL = 'users.CustomUser'
  ```
- Implement authentication views (login, register, logout)
- Templates: `register.html`, `login.html`, `logout.html`

### 3. Product Management
- `Product` model includes `seller`, `name`, `description`, `price`, `image`, `rating`, and `stock`
- Views: `product_list`, `add_product`, `edit_product`, `delete_product`, `seller_products`
- Templates: `products_list.html`, `product_form.html`, `seller_products.html`

### 4. Cart System
- Use Django sessions to store cart as a dictionary
- Views:
  - `add_to_cart(product_id)`
  - `remove_from_cart(product_id)`
  - `view_cart()`
- Template: `cart.html`

### 5. Order Management
- `Order` model: buyer, product, quantity, status, order_date
- Views:
  - `checkout()`
  - `my_orders()` — for buyers
  - `seller_orders()` — for sellers
- Templates: `checkout.html`, `my_orders.html`, `seller_orders.html`

### 6. Dashboard
- Views and templates restricted to sellers
- `dashboard_home()` view shows product and order links
- Template: `dashboard_home.html`

### 7. Templates & Routing
- Root `templates/` directory registered in settings:
  ```python
  TEMPLATES = [{
      'DIRS': [BASE_DIR / 'templates'],
      ...
  }]
  ```
- Use `include()` in project `urls.py`:
  ```python
  path('products/', include('products.urls')),
  path('orders/', include('orders.urls')),
  path('dashboard/', include('dashboard.urls')),
  path('accounts/', include('users.urls')),
  ```

### 8. Admin Setup
- Register models in `admin.py` of each app
- Create admin user:  
  ```bash
  python manage.py createsuperuser
  ```

### 9. Static Files and Styling
- Add `style.css` under `static/css/`
- Update `base.html` to load static files:  
  ```django
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  ```

## Sample base.html with Styling
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}E-Commerce{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <header>
        <h1>Welcome to the E-Commerce Platform</h1>
        {% if user.is_authenticated %}
            <p>Hello, {{ user.username }}!</p>
        {% endif %}
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

## Conclusion
This Django project supports a complete e-commerce flow with clear separation of roles, session-based cart management, custom dashboards, and visual styling for a better user experience.
