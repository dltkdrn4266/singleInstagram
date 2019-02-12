from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})

post_detail = PostView.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'posts/', post_list, name='post_list'),
    url(r'posts/<int:pk>/', post_detail, name='post_detail')
])
