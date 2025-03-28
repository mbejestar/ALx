from django.db import models  
from django.contrib.auth import get_user_model  
from django.contrib.contenttypes.fields import GenericForeignKey  
from django.contrib.contenttypes.models import ContentType  

User = get_user_model()  

class Notification(models.Model):  
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)  
    actor = models.ForeignKey(User, related_name='actor_notifications', on_delete=models.CASCADE)  
    verb = models.CharField(max_length=255)  # e.g., "liked", "commented"  
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  
    target_object_id = models.PositiveIntegerField()  
    target = GenericForeignKey('target_content_type', 'target_object_id')  
    timestamp = models.DateTimeField(auto_now_add=True)  
    read = models.BooleanField(default=False)  

    def __str__(self):  
        return f'Notification: {self.actor} {self.verb} {self.target}'  