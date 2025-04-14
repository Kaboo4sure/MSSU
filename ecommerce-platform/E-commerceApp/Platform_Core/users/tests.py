from django.contrib.auth import get_user_model
from django.test import TestCase

class UserAuthTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='buyer1', password='testpass123')
        self.assertEqual(user.username, 'buyer1')
        self.assertTrue(user.check_password('testpass123'))

    def test_login(self):
        self.client.post('/register/', {'username': 'testuser', 'password': 'pass123'})
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'pass123'})
        self.assertEqual(response.status_code, 200)
