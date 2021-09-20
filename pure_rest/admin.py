from django.contrib import admin
from .models import Book, Author, Publisher

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pages', 'price', 'rating', 'pubdate')
    list_filter = ('author', 'publisher')


class AuthorAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'age']


class PublisherAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)