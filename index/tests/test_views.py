from django.test import Client, TestCase
from django.urls import reverse

from index.models import ToDo

class BlogTests(TestCase):

    def home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def blog_detail_view(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code,200)

    def test_post_creation(self):
        c = Client()
        response = c.post('/post/new/',{'title': 'new title', 'body':'new text'})
        self.assertEqual(response.status_code, 200)