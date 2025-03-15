from rest_framework import serializers  
from .models import Author, Book  

class BookSerializer(serializers.ModelSerializer): 

   """  
    Serializer for the Book model; validates publication year.  
    """  
    
    class Meta:  
        model = Book  
        fields = ['id', 'title', 'publication_year', 'author']  

    def validate_publication_year(self, value):  
        if value > timezone.now().year:  
            raise serializers.ValidationError("Publication year cannot be in the future.")  
        return value  

class AuthorSerializer(serializers.ModelSerializer): 

"""  
    Serializer for the Author model; includes nested Book serialization.  
    """  
   
    books = BookSerializer(many=True, read_only=True)  

    class Meta:  
        model = Author  
        fields = ['id', 'name', 'books']  