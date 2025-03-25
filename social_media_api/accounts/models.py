from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Users biography
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile pictureupload
    following = models.ManyToManyField(
        'self',  # Self-referential relationship
        symmetrical=False,  
        related_name='followers',  # Reverse relationship for followers
        blank=True
    )

    def __str__(self):
        return self.username

#views in the accounts app that allow users to follow and unfollow others. 

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

CustomUser  = get_user_model()

class UserListView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        user_data = [{'id': user.id, 'username': user.username} for user in users]
        return Response(user_data)
