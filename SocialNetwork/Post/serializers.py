from rest_framework import serializers
from .models import *


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title', 'content', 'user')


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')


class LikeDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('__all__')