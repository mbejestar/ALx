from rest_framework import generics  
from .models import Book  
from .serializers import BookSerializer  

class BookList(generics.ListAPIView):  
    queryset = Book.objects.all()  # Retrieve all Book objects  
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data  