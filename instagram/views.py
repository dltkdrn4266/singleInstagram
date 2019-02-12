from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PostSerializer

#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializers = PostSerializer(queryset, many=True)
#         return Response(serializers.data)

#     def post(self, request, format=None):
#         serializers = PostSerializer(data=request.data)
#         if serializers.is_vaild():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    
# class PostDetail(viewsets.ModelViewSet):
#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404

#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

