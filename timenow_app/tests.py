from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomeTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('index')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_page(self):
        url = reverse('index')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'timenow_app/index.html')