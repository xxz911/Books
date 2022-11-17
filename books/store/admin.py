from .models import Book, UserBookRelation
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'author_name', 'owner')
    list_display_links = ('name', 'price', 'author_name')


class UserBookRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'like', 'in_bookmarks', 'rate')


admin.site.register(Book, BookAdmin)
admin.site.register(UserBookRelation, UserBookRelationAdmin)
