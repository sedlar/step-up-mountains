from django.test import TestCase
from django.test import Client
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Account(TestCase):
    def setUp(self):
        self.client = Client()
        setup_test_environment()
        self.testpassword = 'testpassword'
        self.testuser = User.objects.create_user('testuser', 'lennon@thebeatles.com', self.testpassword)
        self.testuser.save()

    def test_login(self):
        """
        Check user can log in
        """
        response = self.client.get(reverse('stepupmountains:accounts:login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('stepupmountains:accounts:login'), {'username': self.testuser.username, 'password': self.testpassword})
        self.assertRedirects(response, reverse('stepupmountains:mountain_list'))
        self.assertEqual(self.testuser.is_authenticated(), True)

