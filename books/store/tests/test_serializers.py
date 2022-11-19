from django.db.models import Count, Case, When, Avg, F
from django.test import TestCase

from django.contrib.auth.models import User

from store.serializers import BooksSerializer
from store.models import Book, UserBookRelation


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_user', first_name='Ivan', last_name="Petrov")
        self.user2 = User.objects.create(username='test_user2', first_name='Max', last_name="Popov")
        self.user3 = User.objects.create(username='test_user3', first_name='1', last_name="2")

        book_1 = Book.objects.create(name='Test book 1', price=25, author_name="Max", owner=self.user)

        book_2 = Book.objects.create(name='Test book 2', price=45, author_name="Max1")

        UserBookRelation.objects.create(user=self.user, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=self.user2, book=book_1, like=True, rate=5)
        user_book_3 = UserBookRelation.objects.create(user=self.user3, book=book_1, like=True)
        user_book_3.rate = 4
        user_book_3.save()

        UserBookRelation.objects.create(user=self.user, book=book_2, like=True, rate=3)
        UserBookRelation.objects.create(user=self.user2, book=book_2, like=True, rate=4)
        UserBookRelation.objects.create(user=self.user3, book=book_2, like=False)

        books = Book.objects.all().annotate(annotated_likes=Count(Case(When(
        userbookrelation__like=True, then=1))),
        owner_name=F('owner__username')).prefetch_related('readers').order_by('id')

        data = BooksSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Max',
                # 'likes_count': 3,
                'annotated_likes': 3,
                'rating': '4.67',
                'owner_name': 'test_user',
                'readers': [
                    {
                        'first_name': 'Ivan',
                        'last_name': 'Petrov'
                    },
                    {
                        'first_name': 'Max',
                        'last_name': 'Popov'
                    },
                    {
                        'first_name': '1',
                        'last_name': '2'
                    },
                ]
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '45.00',
                'author_name': 'Max1',
                # 'likes_count': 2,
                'annotated_likes': 2,
                'rating': '3.50',
                'owner_name': None,
                'readers': [
                    {
                        'first_name': 'Ivan',
                        'last_name': 'Petrov'
                    },
                    {
                        'first_name': 'Max',
                        'last_name': 'Popov'
                    },
                    {
                        'first_name': '1',
                        'last_name': '2'
                    },
                ]
            }
        ]
        print(data)
        print(expected_data)
        self.assertEqual(expected_data, data)

