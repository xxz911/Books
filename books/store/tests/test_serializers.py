from unittest import TestCase

from django.contrib.auth.models import User

from store.serializers import BooksSerializer
from store.models import Book


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_username')
        book_1 = Book.objects.create(name='Test book 1', price=25, author_name="Max", owner=self.user)
        print(book_1.owner.pk)
        book_2 = Book.objects.create(name='Test book 2', price=45, author_name="Max1", owner=self.user)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Max',
                'owner': book_1.owner.pk

            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '45.00',
                'author_name': 'Max1',
                'owner': book_1.owner.pk
            }
        ]
        print(data)
        self.assertEqual(expected_data, data)
