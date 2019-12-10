from django.test import TestCase, Client

from index.models import ToDo



class BlogTests(TestCase):

    def setUp(self):
        self.post = ToDo.objects.create(
            title = 'cleaning room',
            body =' you have to clean your room'
            )

    def test_ToDo_Creation(self):
        '''Test testing the dunder method on the post'''
        post = ToDo(title = 'another one')
        self.assertEqual(post.__str__(),post.title)
