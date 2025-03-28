from rest_framework import viewsets  
from rest_framework.permissions import IsAuthenticated  
from .models import Notification  
from .serializers import NotificationSerializer  

class NotificationViewSet(view