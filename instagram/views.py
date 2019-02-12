from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializers_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializers):
        serializers.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PostSerializer

    @api_view(['GET', 'POST'])
    def get_post_list(request):
        if request.method == 'GET':
            serializers = PostSerializer(queryset, many=True)
            return Response(serializers.data)

        elif request.method == 'POST':
            serializers = PostSerializer(data=request.data)
            if serializers.is_vaild():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    def post_detail(request):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

