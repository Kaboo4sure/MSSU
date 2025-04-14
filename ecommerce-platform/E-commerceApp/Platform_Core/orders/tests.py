from django.test import TestCase
from products.models import Product

class CartTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Shoes', price=75.00)

    def test_add_to_cart(self):
        session = self.client.session
        session['cart'] = {}
        session.save()
        response = self.client.get(f'/cart/add/{self.product.id}/')
        self.assertEqual(response.status_code, 302)

