from django.shortcuts import render, redirect

# Create your views here.
from library.forms import BookForm


def index(request):
    return render(request, 'sw1/index.html')


def create_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
    # TODO implement front
    return render(request, 'sw1/book_creation.html')

