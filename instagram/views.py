from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, FileUploaderSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.multipartparser import MultiPartParser
from rest_framework.parsers import FormParser

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PostSerializer

# class FileUploaderViewSet(viewsets.ModelViewSet):
#     serializer_class = FileUploaderSerializer
#     parser_classes = (MultiPartParser, FormParser,)

#     queryset = LayerFile.objects.all()

#     def get_queryset(self, *args, **kwargs):
#         qs = super(FileUploaderViewSet, self).get_queryset(*args, **kwargs)
#         qs = qs.filter(owner=self.request.user)

#         return qs