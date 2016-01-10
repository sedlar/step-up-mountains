from django.test import TestCase
from django.test import Client
from django.test.utils import setup_test_environment
from stepupmountains.models import ClimbingObject
from stepupmountains.models import Mountain
from stepupmountains.models import Climb
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from stepupmountains.mountains import add_climbed_attribute_to_all
import datetime
from django.utils import timezone
from stepupmountains.climbs import get_fastest_climb, get_all_climbs, format_fastest_climb
from time import sleep
from datetime import timedelta
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

    def test_fastest_climb(self):
        """
        Check simple fastest climb calculation
        """
        self.testpassword = 'testpassword'
        self.testuser = User.objects.create_user('UliSnek', 'lennon@thebeatles.com', self.testpassword)
        self.testuser.save()
        self.climbing_object1 = ClimbingObject(user = self.testuser, name = 'test_object', height = 1000, order = 0)
        self.climbing_object1.save()

        highest_mountain = Mountain(name='Mount Everest', elevation=8850, comment='Mount Everest comment')
        highest_mountain.save()

        self.climb1 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb1.save()
        sleep(1)
        self.climb2 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb2.save()
        self.climb3 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb3.save()
        self.climb4 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb4.save()
        self.climb5 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb5.save()
        self.climb6 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb6.save()
        self.climb7 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb7.save()
        self.climb8 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb8.save()
        self.climb9 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb9.save()
        self.climb10 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb10.save()
        sleep(1)
        self.climb11 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb11.save()

        self.assertEqual(self.climb10.datetime-self.climb2.datetime, get_fastest_climb(get_all_climbs(self.testuser).order_by('datetime'), highest_mountain))

    def test_fastest_climb_different_heights(self):
        """
        Check simple fastest climb calculation
        """
        self.testpassword = 'testpassword'
        self.testuser = User.objects.create_user('UliSnek', 'lennon@thebeatles.com', self.testpassword)
        self.testuser.save()
        self.climbing_object1 = ClimbingObject(user = self.testuser, name = 'test_object', height = 1000, order = 0)
        self.climbing_object1.save()
        self.climbing_object2 = ClimbingObject(user = self.testuser, name = 'test_object2', height = 4000, order = 0)
        self.climbing_object2.save()

        highest_mountain = Mountain(name='Mount Everest', elevation=8850, comment='Mount Everest comment')
        highest_mountain.save()

        self.climb1 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb1.save()
        self.climb2 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb2.save()
        self.climb3 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb3.save()
        self.climb4 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb4.save()
        self.climb5 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb5.save()
        self.climb6 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb6.save()
        self.climb7 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb7.save()
        self.climb8 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb8.save()
        self.climb9 = Climb(user=self.testuser, climbed_object=self.climbing_object2)
        self.climb9.save()

        self.assertEqual(self.climb9.datetime-self.climb4.datetime, get_fastest_climb(get_all_climbs(self.testuser).order_by('datetime'), highest_mountain))

    def test_fastest_climb_not_climbed(self):
        """
        Check simple fastest climb calculation
        """
        self.testpassword = 'testpassword'
        self.testuser = User.objects.create_user('UliSnek', 'lennon@thebeatles.com', self.testpassword)
        self.testuser.save()
        self.climbing_object1 = ClimbingObject(user = self.testuser, name = 'test_object', height = 1000, order = 0)
        self.climbing_object1.save()

        highest_mountain = Mountain(name='Mount Everest', elevation=8850, comment='Mount Everest comment')
        highest_mountain.save()

        self.climb1 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb1.save()
        self.climb2 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb2.save()
        self.climb3 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb3.save()
        self.climb4 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb4.save()
        self.climb5 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb5.save()
        self.climb6 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb6.save()
        self.climb7 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb7.save()
        self.climb8 = Climb(user=self.testuser, climbed_object=self.climbing_object1)
        self.climb8.save()

        fastest_climb = get_fastest_climb(get_all_climbs(self.testuser).order_by('datetime'), highest_mountain)
        self.assertEqual(timedelta.max, fastest_climb)
        self.assertEqual("N/A", format_fastest_climb(fastest_climb))
