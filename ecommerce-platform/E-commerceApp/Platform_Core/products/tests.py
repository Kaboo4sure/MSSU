from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from products.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.seller = User.objects.create_user(
            username='seller1',
            password='pass123',
            role='seller'
        )
        self.client.login(username='seller1', password='pass123')

    def test_add_product(self):
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61',  # fake GIF header bytes
            content_type='image/gif'
        )

        response = self.client.post(reverse('add-product'), {
            'name': 'Test Product',
            'price': 50.00,
            'stock': 10,
            'description': 'Test description',
            'image': image
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Test Product').exists())

    def test_product_list_view(self):
        Product.objects.create(
            name='List Product',
            price=20.00,
            stock=5,
            description='Visible product',
            seller=self.seller
        )
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'List Product')
