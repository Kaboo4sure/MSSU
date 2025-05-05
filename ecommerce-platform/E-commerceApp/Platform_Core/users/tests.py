from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class UserAuthTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='buyer1', password='testpass123')
        self.assertEqual(user.username, 'buyer1')
        self.assertTrue(user.check_password('testpass123'))

    def test_register_and_login(self):
        # Register user
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'strongpass123',
            'password2': 'strongpass123',
            'role': 'buyer'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to 'home'
        
        # Login user
        login_response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'strongpass123'
        })
        self.assertEqual(login_response.status_code, 302)  # Should redirect to 'home'

    def test_profile_update_page_access(self):
        User = get_user_model()
        user = User.objects.create_user(username='profileuser', password='123pass', role='buyer')
        self.client.login(username='profileuser', password='123pass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
