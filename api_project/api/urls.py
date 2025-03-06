from django.urls import path, include  
from rest_framework import routers  
from .views import BookList, BookViewSet  

router = routers.DefaultRouter()  
router.register(r'books_all', BookViewSet, basename='book_all')  

urlpatterns = [  
    path('books/', BookList.as_view(), name='book-list'), #Keep the old route  
    path('', include(router.urls)),  
]  