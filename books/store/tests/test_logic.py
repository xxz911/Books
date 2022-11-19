from django.test import TestCase

from django.contrib.auth.models import User

from store.logic import set_rating
from store.models import Book, UserBookRelation


class SetRatingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', first_name='Ivan', last_name="Petrov")
        self.user2 = User.objects.create(username='test_user2', first_name='Max', last_name="Popov")
        self.user3 = User.objects.create(username='test_user3', first_name='1', last_name="2")

        self.book_1 = Book.objects.create(name='Test book 1', price=25, author_name="Max", owner=self.user)

        UserBookRelation.objects.create(user=self.user, book=self.book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=self.user2, book=self.book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=self.user3, book=self.book_1, like=True, rate=4)

    def test_ok(self):
        set_rating(self.book_1)
        self.book_1.refresh_from_db()
        self.assertEqual('4.67', str(self.book_1.rating))

