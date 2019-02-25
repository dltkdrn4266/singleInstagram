from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.multipartparser import MultiPartParser

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PostSerializer