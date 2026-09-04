from django.urls import resolve
from lists.views import home_page
from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post(
            '/',
            data={'item_text': 'A new list item'}
        )

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_be_loaded_with_GET(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)