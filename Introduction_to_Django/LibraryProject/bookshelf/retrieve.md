# Retrieve Book Example  

## Run the following commands in the Django shell:  

```python  
from bookshelf.models import Book  

# Retrieve the book  
book = Book.objects.get(title="1984")  # Ensure this title exists in the database  

# Print the details  
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
