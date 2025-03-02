from django.db import models  
from django.contrib.auth.models import AbstractUser, BaseUserManager  
from django.conf import settings  

# Custom User Manager  
class CustomUserManager(BaseUserManager):  
    """Custom user manager to handle user creation with email instead of username."""  

    def create_user(self, username, email, password=None, **extra_fields):  
        if not email:  
            raise ValueError("The Email field must be set")  
        email = self.normalize_email(email)  
        extra_fields.setdefault("is_active", True)  
        user = self.model(username=username, email=email, **extra_fields)  
        user.set_password(password)  
        user.save(using=self._db)  
        return user  

    def create_superuser(self, username, email, password=None, **extra_fields):  
        extra_fields.setdefault("is_staff", True)  
        extra_fields.setdefault("is_superuser", True)  

        if extra_fields.get("is_staff") is not True:  
            raise ValueError("Superuser must have is_staff=True.")  
        if extra_fields.get("is_superuser") is not True:  
            raise ValueError("Superuser must have is_superuser=True.")  

        return self.create_user(username, email, password, **extra_fields)  

# Custom User Model  
class CustomUser(AbstractUser):  
    date_of_birth = models.DateField(null=True, blank=True)  
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  

    objects = CustomUserManager()  

    def __str__(self):  
        return self.username  

# UserProfile Model  
class UserProfile(models.Model):  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelf_profile')  
    bio = models.TextField(blank=True, null=True)  
    location = models.CharField(max_length=255, blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  

    def __str__(self):  
        return self.user.username  

# Book Model with Permissions  
class Book(models.Model):  
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100)  
    publication_year = models.IntegerField()  

    class Meta:  
        permissions = [  
            ("can_view", "Can view book"),  
            ("can_create", "Can create book"),  
            ("can_edit", "Can edit book"),  
            ("can_delete", "Can delete book"),  
        ]  

    def __str__(self):  
        return self.title  

# Library Model with Many-to-Many Relationship  
class Library(models.Model):  
    name = models.CharField(max_length=255)  
    location = models.CharField(max_length=255)  
    books = models.ManyToManyField(Book, through='LibraryBook')  # Linking Library and Book  

    def __str__(self):  
        return self.name  

# LibraryBook Model Linking Library and Book  
class LibraryBook(models.Model):  
    library = models.ForeignKey(Library, on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)  
    added_at = models.DateTimeField(auto_now_add=True)  

    class Meta:  
        unique_together = ('library', 'book')  

    def __str__(self):  
        return f"{self.library.name} - {self.book.title}"  

# Author Model  
class Author(models.Model):  
    name = models.CharField(max_length=100, unique=True)  

    def __str__(self):  
        return self.name
