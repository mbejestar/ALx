from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import permission_required  
from .models import Book  
from .forms import BookForm  # Assume you have a form for creating/editing books  

# View to list all books  
@permission_required('your_app_name.can_view', raise_exception=True)  
def book_list(request):  
    books = Book.objects.all()  
    return render(request, 'book_list.html', {'books': books})  

# View to create a new book  
@permission_required('your_app_name.can_create', raise_exception=True)  
def book_create(request):  
    if request.method == 'POST':  
        form = BookForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('book_list')  # redirect to book list after creation  
    else:  
        form = BookForm()  
    return render(request, 'book_form.html', {'form': form})  

# View to edit an existing book  
@permission_required('your_app_name.can_edit', raise_exception=True)  
def book_edit(request, book_id):  
    book = get_object_or_404(Book, id=book_id)  
    if request.method == 'POST':  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            form.save()  
            return redirect('book_list')  # redirect to book list after editing  
    else:  
        form = BookForm(instance=book)  
    return render(request, 'book_form.html', {'form': form, 'book': book})  

# View to delete a specific book  
@permission_required('your_app_name.can_delete', raise_exception=True)  
def book_delete(request, book_id):  
    book = get_object_or_404(Book, id=book_id)  
    if request.method == 'POST':  
        book.delete()  
        return redirect('book_list')  # redirect to book list after deletion  
    return render(request, 'book_confirm_delete.html', {'book': book})
