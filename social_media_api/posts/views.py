from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(author__in=following_users).order_by
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics  # Importing generics for better object retrieval
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def like_post(request, pk):
    # Using generics.get_object_or_404 to fetch the post
    post = generics.get_object_or_404(Post, pk=pk)
    
    # Get or create a like object for the user and the post
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    # If the like was not created (meaning it already exists), return a message
    if not created:
        return Response({'message': 'You have already liked this post!.'}, status=400)

    # Create a notification for the post author
    notification = Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked',
        target=post
    )

    return Response({'message': f'You liked {post.title}'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def unlike_post(request, pk):
    # Using generics.get_object_or_404 to fetch the post
    post = generics.get_object_or_404(Post, pk=pk)
    
    # Find the like object associated with the user and the post
    like = Like.objects.filter(user=request.user, post=post).first()
    
    if not like:
        return Response({'message': 'You haven't liked this post yet.'}, status=400)
    
    # Remove the like
    like.delete()

    return Response({'message': f'You just unliked : {post.title}'}, status=200)
