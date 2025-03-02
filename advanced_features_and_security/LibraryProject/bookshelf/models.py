from django.db import models  
from django.contrib.auth.models import AbstractUser, BaseUserManager  

# Custom User Manager  
class CustomUserManager(BaseUserManager):  
    def create_user(self, email, password=None, **extra_fields):  
        """Create and return a regular user with an email and password."""  
        if not email:  
            raise ValueError('The Email field must be set')  
        email = self.normalize_email(email)  
        user = self.model(email=email, **extra_fields)  
        user.set_password(password)  
        user.save(using=self._db)  
        return user  

    def create_superuser(self, email, password=None, **extra_fields):  
        """Create and return a superuser with an email and password."""  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  

        return self.create_user(email, password, **extra_fields)  

# Custom User Model  
class CustomUser(AbstractUser):  
    date_of_birth = models.DateField(null=True, blank=True)  
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  

    # Use the custom user manager  
    objects = CustomUserManager()

###
class Article(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    
    class Meta:  
        permissions = [  
            ("can_view", "Can view article"),  
            ("can_create", "Can create article"),  
            ("can_edit", "Can edit article"),  
            ("can_delete", "Can delete article"),  
        ]  
