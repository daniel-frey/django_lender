from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book


def book_detail_view(request, pk=None):
    """detail view of the book. List of all available fields."""
    context = {
        'book': get_object_or_404(Book, id=pk)
    }

    return render(request, 'books/book_detail.html', context)


def book_list_view(request):
    """List view will display all of the books in the database."""
    context = {
        'books': get_list_or_404(Book)
    }

    return render(request, 'books/book_list.html', context)
