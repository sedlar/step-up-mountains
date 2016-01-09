from django.test import TestCase
from django.test import Client
from django.test.utils import setup_test_environment
from stepupmountains.models import ClimbingObject
from stepupmountains.models import Mountain
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from stepupmountains.mountains import add_climbed_attribute_to_all
#from unittest import skip

# Create your tests here.
class SmokeTests(TestCase):
    def setUp(self):
        self.client = Client()
        setup_test_environment()
        self.testpassword = 'testpassword'
        self.testuser = User.objects.create_user('testuser', 'lennon@thebeatles.com', self.testpassword)
        self.testuser.save()
        self.climbing_object = ClimbingObject(user = self.testuser, name = 'test_object', height = 500, order = 0)
        self.climbing_object.save()
        Mountain(name='Mount Everest', elevation=8850, comment='Mount Everest comment').save()
        Mountain(name='Praded', elevation=1492, comment='Praded comment').save()
        Mountain(name='Rampach', elevation=442, comment='Vlnak na Hane').save()

    def test_show_mountain_list_no_login(self):
        all_mountains = Mountain.objects.order_by('-elevation');
        add_climbed_attribute_to_all(all_mountains, 0)

        response = self.client.get(reverse('stepupmountains:mountain_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mountain_list'], [repr(r) for r in all_mountains])
                
    def test_show_mountain_list_no_climb(self):
        """
        Check that mountain_list view is displayed
        """
        self.client.login(username=self.testuser.username, password=self.testpassword)

        all_mountains = Mountain.objects.order_by('-elevation');
        add_climbed_attribute_to_all(all_mountains, 0)


        response = self.client.get(reverse('stepupmountains:mountain_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mountain_list'], [repr(r) for r in all_mountains])
#check reached mountain
        self.assertEqual(response.context['reached_mountain'].name, 'None')
        self.assertEqual(response.context['reached_mountain'].elevation, 0)
#check next mountain
        self.assertEqual(response.context['next_mountain'], 'Rampach')
        self.assertEqual(response.context['remains_to_climb'], 442)

    def test_show_mountain_list_climbed(self):
        """
        Check that mountain_list view is displayed
        """
#SetUp
        self.client.login(username=self.testuser.username, password=self.testpassword)

        button_caption = 'Climb ' + self.climbing_object.name
        response = self.client.post(reverse('stepupmountains:climb_object'), {'climbed_object': self.climbing_object.id, 'Climb': button_caption})
        self.assertRedirects(response, reverse('stepupmountains:mountain_list_args', kwargs={'climbed': self.climbing_object.name}))

        all_mountains = Mountain.objects.order_by('-elevation');
        add_climbed_attribute_to_all(all_mountains, 0)

#Test
        response = self.client.get(reverse('stepupmountains:mountain_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['mountain_list'], [repr(r) for r in all_mountains])
#check reached mountain
        self.assertEqual(response.context['reached_mountain'].name, 'Rampach')
        self.assertEqual(response.context['reached_mountain'].elevation, 442)
#check next mountain
        self.assertEqual(response.context['next_mountain'], 'Praded')
        self.assertEqual(response.context['remains_to_climb'], 1492-self.climbing_object.height)

    def test_login(self):
        """
        Check user can log in
        """
        Mountain(name='Mount Everest', elevation=8850, comment='Mount Everest comment').save()
        response = self.client.get(reverse('stepupmountains:accounts:login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('stepupmountains:accounts:login'), {'username': self.testuser.username, 'password': self.testpassword})
        self.assertRedirects(response, reverse('stepupmountains:mountain_list'))
        self.assertEqual(self.testuser.is_authenticated(), True)

    def test_climb(self):
        """
        Check that user can climb
        """
        self.client.login(username=self.testuser.username, password=self.testpassword)

        response = self.client.get(reverse('stepupmountains:mountain_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('total_climbed' in response.context)
        ascent = response.context['total_climbed']
        self.assertEqual(ascent, 0.0)

        button_caption = 'Climb ' + self.climbing_object.name
        response = self.client.post(reverse('stepupmountains:climb_object'), {'climbed_object': self.climbing_object.id, 'Climb': button_caption})
        self.assertRedirects(response, reverse('stepupmountains:mountain_list_args', kwargs={'climbed': self.climbing_object.name}))

        response = self.client.get(reverse('stepupmountains:mountain_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('total_climbed' in response.context)
        new_ascent = response.context['total_climbed']
        self.assertEqual(ascent+self.climbing_object.height, new_ascent)

