from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import BookForm
# bookshelf/views.py
from django.views.decorators.http import require_http_methods
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """Display a list of books (only accessible to users with 'can_view' permission)."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})



@require_http_methods(["GET", "POST"])
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # Safe ORM usage
            book = form.save(commit=False)
            book.added_by = request.user  # Track user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})


def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
