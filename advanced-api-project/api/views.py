from rest_framework import generics, filters  
from django_filters.rest_framework import DjangoFilterBackend  
from .models import Book  
from .serializers import BookSerializer  
from .filters import BookFilter  

class BookListView(generics.ListAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  
    filterset_class = BookFilter  
    search_fields = ['title', 'author__name']  # Enable search on title and author name  
    ordering_fields = ['title', 'publication_year']  # Enable ordering on title and publication year  
    ordering = ['title']  # Default ordering by title
