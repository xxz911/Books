from unittest import TestCase

from store.serializers import BooksSerializer
from store.models import Book


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price=25, author_name="Max")
        book_2 = Book.objects.create(name='Test book 2', price=45, author_name="Max1")
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Max',

            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '45.00',
                'author_name': 'Max1',

            }
        ]
        self.assertEqual(expected_data, data)
