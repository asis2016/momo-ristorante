from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Blog

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Blog.objects.create(
            title='A good title',
            excerpt='Nice excerpt content',
            content='Testing content',
            user=self.user,
            create_date='2020-2-1'
        )

    #def test_post_detail_view(self):
        #response = self.client.get('/blog/1/')