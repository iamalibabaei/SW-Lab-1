from django.urls import path

from library.views import index, create_book, list_book

urlpatterns = [
    path('', index),
    path('add', create_book),
    path('list', list_book),
]
