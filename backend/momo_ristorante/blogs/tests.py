from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Blog


class BlogTestCase(TestCase):
    """ Test case for Blog. """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Blog.objects.create(
            user=self.user,
            title='new title',
            excerpt='',
            content='some content',
            image='',
            create_date='2021-1-1'
        )

    def test_blog_page(self):
        """
        Test if /blog/ exists.
        Test if blog/index.html exists.
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        """  """
        self.assertTemplateUsed(response, template_name='blogs/index.html')

    def test_blog_page_item_status_code(self):
        """
        Test if /blog/1/ exists.
        Test if /blog/1/ template exists.
        """
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get('/blog/1000/')
        self.assertEqual(no_response.status_code, 404)

        self.assertTemplateUsed(response, template_name='blogs/detail.html')
