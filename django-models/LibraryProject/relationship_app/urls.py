from django.urls import path
from .views import LibraryDetailView, home_view
from .views import list_books
from .views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from . import views
from .views import add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView
from .views import LibraryDetailView, home_view, list_books, admin_view, librarian_view, member_view, add_book, edit_book, delete_book


urlpatterns = [
    path("login/", LoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='relationship_app/logout.html'), name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.home_view, name="home"),
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('books/<int:book_id>/', delete_book, name='delete_book'),
]
