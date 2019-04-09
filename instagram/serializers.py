from rest_framework import serializers
from .models import Post, Comment, MarkerGps
from django.contrib.auth.models import User
import os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
    
class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)
        return super(Base64ImageField, self).to_internal_value(data)
    
    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class MarkerGpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkerGps
        fields = ('latitude','longitude')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    photos = Base64ImageField(
        max_length=None, use_url=True,
    )
    gps = MarkerGpsSerializer()
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'photos',
            'gps',
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


    
