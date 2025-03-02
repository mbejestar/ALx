from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Define roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# 1. ForeignKey Relationship
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title

# 2. ManyToMany Relationship
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name

# 3. OneToOne Relationship
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='librarian'
    )
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_add_library", "Can add library"),
            ("can_change_library", "Can change library"),
            ("can_delete_library", "Can delete library"),
        ]
