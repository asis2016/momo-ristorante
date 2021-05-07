from django.test import TestCase
from django.urls import reverse


class WebsiteTests(TestCase):

    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get('about.html')
        self.assertEqual(response.status_code, 200)
