from django.shortcuts import render, redirect

# Create your views here.
from library.forms import BookForm
from library.models import Book


def index(request):
    return render(request, 'sw1/index.html')


def create_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()

    return render(request, 'sw1/book_creation.html')
def list_book(request):
    books = Book.objects.all()
    # TODO implement lists show
    return render(request, 'sw1/list.html')
