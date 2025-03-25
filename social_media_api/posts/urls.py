from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configure Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",  # Title of the API
        default_version='v1',  # API version
        description="API for managing posts and comments",  # Description of the API
    ),
    public=True,  # Set the schema to be publicly accessible
    permission_classes=(permissions.AllowAny,),  # Allow access without authentication
)



from django.urls import path
from .views import user_feed

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/like/', views.like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]

