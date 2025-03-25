from django.urls import path
from .views import follow_user, unfollow_user, UserListView

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('users/', UserListView.as_view(), name='user-list'),
]
