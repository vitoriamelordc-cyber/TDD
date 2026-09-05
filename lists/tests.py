from django.test import TestCase
from .models import Item


class HomePageTest(TestCase):

    def test_home_page_can_be_loaded_with_GET(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={
            'item_text': 'A new list item'
        })

        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()

        self.assertEqual(new_item.text, 'A new list item')

    def test_can_save_multiple_items(self):
        self.client.post('/', data={
            'item_text': 'A new list item'
        })

        self.client.post('/', data={
            'item_text': 'Another list item'
        })

        self.assertEqual(Item.objects.count(), 2)

        first_item = Item.objects.all()[0]
        second_item = Item.objects.all()[1]

        self.assertEqual(first_item.text, 'A new list item')
        self.assertEqual(second_item.text, 'Another list item')