from django.test import TestCase, Client
from urllib import response
from django.urls import resolve

# Create your tests here.
class TestUrl(TestCase):
    def testing_html(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def testing_xml(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    
    def testing_json(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
