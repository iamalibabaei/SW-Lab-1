from django.urls import path

from library.views import index, create_book, list_book

urlpatterns = [
    path('', index),
    path('add', create_book),
    path('lsit', list_book),
]
