from django.test import TestCase
from django import http
# Create your tests here.

from . import views

class HomeViewTest(TestCase):
    def test_home(self):
        requst = http.HttpRequest()
        response = views.home(request)
        self.assertEqual(200, response.status_code)
        self.assertIn('Works', response.content)
