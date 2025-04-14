from django.test import TestCase
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()

class ProductTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='seller1', password='pass123')

    def test_add_product(self):
        self.client.login(username='seller1', password='pass123')
        response = self.client.post('/products/add/', {
            'name': 'Test Product',
            'price': 50.00,
            'stock': 10,
            'description': 'A product for test'
        })
        self.assertEqual(response.status_code, 302)  # redirect on success

    def test_product_str(self):
        product = Product(name='Item', price=10.00)
        self.assertEqual(str(product), 'Item')

