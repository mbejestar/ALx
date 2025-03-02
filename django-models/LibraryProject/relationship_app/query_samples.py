import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author using ForeignKey"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using reverse relationship
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found")

def list_books_in_library(library_name):
    """List all books in a library using ManyToMany"""
    try:
        library = Library.objects.get(name=library_name)  # <-- Explicit objects.get
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found")

def retrieve_librarian_for_library(library_name):
    """Retrieve librarian for a library using OneToOne"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library_name}")

if __name__ == "__main__":
    # Example usage
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
