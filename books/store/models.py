from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    author_name = models.CharField(max_length=255, verbose_name="Автор")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books', verbose_name="Владелец")
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books', verbose_name="Читатели")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'
        ordering = ['id']


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name="Пользователь")
    book = models.ForeignKey(Book, on_delete=models.CASCADE,  verbose_name="Книга")
    like = models.BooleanField(default=False,  verbose_name="Лайк")
    in_bookmarks = models.BooleanField(default=False,  verbose_name="Избранное")
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True, blank=True, verbose_name="Оценка")

    def __str__(self):
        return f' {self.user.username}: {self.book.name}'

    class Meta:
        verbose_name = 'Отношениe Пользователя'
        verbose_name_plural = 'Отношения Пользователей'
        ordering = ['id']

