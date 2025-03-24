from rest_framework import serializers  
from .models import CustomUser  

class CustomUserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = CustomUser  
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']  
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):  
        user = CustomUser(**validated_data)  
        user.set_password(validated_data['password'])  
        user.save()  
        return user  