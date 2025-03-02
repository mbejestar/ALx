from bookshelf.models import Book  

# Retrieve the book (Make sure you get the correct one)  
try:  
    book = Book.objects.get(title="1984")  # Ensure this title exists in the database  
    # Delete the book  
    book.delete()  

    # Confirm deletion by checking if any books remain  
    print(Book.objects.all())  # <QuerySet []> if the book was successfully deleted  
except Book.DoesNotExist:  
    print("Book with title '1984' does not exist.")
