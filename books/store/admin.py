from .models import Book
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'author_name', 'owner')
    list_display_links = ('name', 'price', 'author_name')


admin.site.register(Book, BookAdmin)
