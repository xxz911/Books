from django.db.models import Count, Case, When, Avg
from django.test import TestCase

from django.contrib.auth.models import User

from store.serializers import BooksSerializer
from store.models import Book, UserBookRelation


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_user')
        self.user2 = User.objects.create(username='test_user2')
        self.user3 = User.objects.create(username='test_user3')

        book_1 = Book.objects.create(name='Test book 1', price=25, author_name="Max")

        book_2 = Book.objects.create(name='Test book 2', price=45, author_name="Max1")

        UserBookRelation.objects.create(user=self.user, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=self.user2, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=self.user3, book=book_1, like=True, rate=4)

        UserBookRelation.objects.create(user=self.user, book=book_2, like=True, rate=3)
        UserBookRelation.objects.create(user=self.user2, book=book_2, like=True, rate=4)
        UserBookRelation.objects.create(user=self.user3, book=book_2, like=False)

        books = Book.objects.all().annotate(annotated_likes=Count(Case(When(
            userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')).order_by('id')

        data = BooksSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Max',
                'likes_count': 3,
                'annotated_likes': 3,
                'rating': '4.67'
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '45.00',
                'author_name': 'Max1',
                'likes_count': 2,
                'annotated_likes': 2,
                'rating': '3.50'

            }
        ]
        self.assertEqual(expected_data, data)
