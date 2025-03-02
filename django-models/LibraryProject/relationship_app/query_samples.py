import os  
import django  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")  
django.setup()  

from relationship_app.models import Author, Book, Library, Librarian  

def query_books_by_author(author_name):  
    authors = Author.objects.filter(name=author_name)  # Use filter to handle multiple authors  
    if authors.exists():  
        for author in authors:  # Iterate through any authors found with that name  
            books = author.books.all()  
            print(f"Books by {author.name}:")  
            for book in books:  
                print(f"- {book.title}")  
    else:  
        print(f"Author {author_name} does not exist.")  

def list_all_books_in_library(library_name):  
    libraries = Library.objects.filter(name=library_name)  # Use filter to handle multiple libraries  
    if libraries.exists():  
        for library in libraries:  # Iterate through any libraries found with that name  
            books = library.books.all()  
            print(f"Books in {library.name}:")  
            for book in books:  
                print(f"- {book.title}")  
    else:  
        print(f"Library {library_name} does not exist.")  

def retrieve_librarian_for_library(library_name):  
    libraries = Library.objects.filter(name=library_name)  # Use filter to handle multiple libraries  
    if libraries.exists():  
        for library in libraries:  # Iterate through any libraries found with that name  
            try:  
                librarian = library.librarian  
                print(f"Librarian for {library.name}: {librarian.name}")  
            except Librarian.DoesNotExist:  
                print(f"No librarian assigned to {library.name}.")  
    else:  
        print(f"Library {library_name} does not exist.")  

if __name__ == "__main__":  
    query_books_by_author("Author Name")  # Replace with actual author name  
    list_all_books_in_library("Library Name")  # Replace with actual library name  
    retrieve_librarian_for_library("Library Name")  # Replace with actual library name
