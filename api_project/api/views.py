from rest_framework import generics  
from rest_framework import viewsets  
from rest_framework import permissions  # Import permissions  
from .models import Book  
from .serializers import BookSerializer  

class BookList(generics.ListAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticated]  


class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Requires Authentication for writing  