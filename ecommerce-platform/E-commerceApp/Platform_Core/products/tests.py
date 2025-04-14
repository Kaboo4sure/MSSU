from django.test import TestCase
from django.contrib.auth import get_user_model

class ProductTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='seller1', password='pass123')
        self.client.login(username='seller1', password='pass123')

    def test_add_product(self):
        response = self.client.post('/products/seller/add/', {
            'name': 'Test Product',
            'price': 50.00,
            'stock': 10,
            'description': 'Test description'
        })
        self.assertEqual(response.status_code, 302)  # redirect on success


