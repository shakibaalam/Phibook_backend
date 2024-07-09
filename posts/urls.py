from django.urls import path
from .views import PostListCreateView, PostDetailView, LikeCreateView, CommentListCreateView, CommentDetailView, random_posts,LikedPostListView,CommentedPostListView


urlpatterns = [
    path('list/', PostListCreateView.as_view(), name='post_list_create'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('user_post_like/', LikedPostListView.as_view(), name='user_post_like'),
    path('user_post_comment/', CommentedPostListView.as_view(), name='user_post_like'),
    path('post_like/<int:post_id>/', LikeCreateView.as_view(), name='like_create'),
    path('post_comment/<int:post_id>/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('post_comment_detail/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('random_posts/', random_posts, name='random_posts'),
]
