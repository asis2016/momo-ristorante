from django.test import TestCase


class WebsiteTests(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
