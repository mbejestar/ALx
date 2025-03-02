# query_samples.py  
import os  
import django  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  
django.setup()  

from relationship_app.models import Author, Book, Library, Librarian  

def query_books_by_author(author_name):  
    try:  
        author = Author.objects.get(name=author_name)  
        books = author.books.all()  
        print(f"Books by {author.name}:")  
        for book in books:  
            print(f"- {book.title}")  
    except Author.DoesNotExist:  
        print(f"Author {author_name} does not exist.")  

def list_all_books_in_library(library_name):  
    try:  
        library = Library.objects.get(name=library_name)  
        books = library.books.all()  
        print(f"Books in {library.name}:")  
        for book in books:  
            print(f"- {book.title}")  
    except Library.DoesNotExist:  
        print(f"Library {library_name} does not exist.")  

def retrieve_librarian_for_library(library_name):  
    try:  
        library = Library.objects.get(name=library_name)  
        librarian = library.librarian  
        print(f"Librarian for {library.name}: {librarian.name}")  
    except Library.DoesNotExist:  
        print(f"Library {library_name} does not exist.")  
    except Librarian.DoesNotExist:  
        print(f"No librarian assigned to {library.name}.")  

if __name__ == "__main__":  
    query_books_by_author("Author Name")  # Replace with actual author name  
    list_all_books_in_library("Library Name")  # Replace with actual library name  
    retrieve_librarian_for_library("Library Name")  # Replace with actual library name