from rest_framework import viewsets, permissions  
from .models import Post, Comment  
from .serializers import PostSerializer, CommentSerializer  

class PostViewSet(viewsets.ModelViewSet):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer  
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):  
        serializer.save(author=self.request.user)  

    def perform_update(self, serializer):  
        post = self.get_object()  
        if post.author == self.request.user:  
            serializer.save()  
        else:  
            self.permission_denied(self.request)  

    def perform_destroy(self, instance):  
        if instance.author == self.request.user:  
            instance.delete()  
        else:  
            self.permission_denied(self.request)  

class CommentViewSet(viewsets.ModelViewSet):  
    queryset = Comment.objects.all()  
    serializer_class = CommentSerializer  
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):  
        post = serializer.validated_data['post']  
        if post.author == self.request.user or post.author in post.followers.all():  
            serializer.save(author=self.request.user)  
        else:  
            self.permission_denied(self.request)  

    def perform_update(self, serializer):  
        comment = self.get_object()  
        if comment.author == self.request.user:  
            serializer.save()  
        else:  
            self.permission_denied(self.request)  

    def perform_destroy(self, instance):  
        if instance.author == self.request.user:  
            instance.delete()  
        else:  
            self.permission_denied(self.request)  