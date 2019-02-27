from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView, CommentView
from instagram import views
from django.urls import path

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})

post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = CommentView.as_view({
    'post': 'create',
    'get': 'list'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('comments/', comment_list, name='comment_list'),
])
