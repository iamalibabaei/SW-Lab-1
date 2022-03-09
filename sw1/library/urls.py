from django.urls import path

from library.views import index, create_book

urlpatterns = [
    path('', index),
    path('add', create_book)
]