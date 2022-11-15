from rest_framework.serializers import ModelSerializer

from .models import Book, UserBookRelation


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ['readers']


class UserBooksRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')