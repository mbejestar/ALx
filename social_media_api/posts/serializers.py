from rest_framework import serializers  
from .models import Post, Comment  

class CommentSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Comment  
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']  
        read_only_fields = ['author', 'created_at', 'updated_at']  

    def create(self, validated_data):  
        user = self.context['request'].user  
        comment = Comment.objects.create(author=user, **validated_data)  
        return comment  

class PostSerializer(serializers.ModelSerializer):  
    comments = CommentSerializer(many=True, read_only=True)  

    class Meta:  
        model = Post  
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']  
        read_only_fields = ['author', 'created_at', 'updated_at']  

    def create(self, validated_data):  
        user = self.context['request'].user  
        post = Post.objects.create(author=user, **validated_data)  
        return post  