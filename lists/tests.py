from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_can_be_loaded_with_GET(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={
            'item_text': 'A new list item'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')