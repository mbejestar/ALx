from rest_framework import generics, permissions  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from rest_framework.authtoken.views import ObtainAuthToken  
from .models import CustomUser  
from .serializers import CustomUserSerializer  

# User Registration View  
class UserRegistrationView(generics.CreateAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserSerializer  
    permission_classes = [permissions.AllowAny]  

    def create(self, request, *args, **kwargs):  
        response = super().create(request, *args, **kwargs)  
        return Response({"token": Token.objects.create(user=self.get_object()).key})  

# Custom Auth Token View  
class CustomAuthToken(ObtainAuthToken):  
    def post(self, request, *args, **kwargs):  
        response = super().post(request, *args, **kwargs)  
        token = Token.objects.get(user=response.data['user'])  
        return Response({'token': token.key})  
