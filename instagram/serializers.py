from rest_framework import serializers
from .models import Post, Comment, FileUploader
from django.contrib.auth.models import User
import os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
    

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    photos = serializers.ImageField(use_url=True)
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

class FileUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploader
        fiedls = (
            'file',
            'name',
            'upload_date',
            'size'
        )
        read_only_fields = ('name','owner','upload_date', 'size')
    
    def validate(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        validated_data['name'] = os.path.splitext(validated_data['file'].name)[0]
        validated_data['size'] = validated_data['file'].size

        return validated_data

    def create(self, validated_data):
        return FileUploader.objects.create(**validated_data)