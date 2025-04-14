from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product

class CartTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.seller = User.objects.create_user(username='seller1', password='pass123')
        self.product = Product.objects.create(
            name='Shoes',
            price=75.00,
            stock=10,
            description='Test shoe',
            seller=self.seller
        )

    def test_add_to_cart(self):
        response = self.client.get(f'/products/add-to-cart/{self.product.id}/')
        self.assertEqual(response.status_code, 302)  # Redirect to cart


