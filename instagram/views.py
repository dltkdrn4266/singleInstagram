from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from .models import Post

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializers_class = PostSerializer
    permission_classes   = (permissions.IsAuthenticated,)

    def perform_create(self, serializers):
        serializers.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PostSerializer