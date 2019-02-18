from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'photos',
            'like',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'content',
            'created_at'
        )