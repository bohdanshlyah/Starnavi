from django.shortcuts import render
from rest_framework import generics
from Post.serializers import *
from .models import *


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeDetailSerializer


class LikeListView(generics.ListAPIView):
    serializer_class = LikeDetailSerializer
    queryset = Like.objects.all()


class LikeDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = LikeDetailSerializer
    queryset = Like.objects.all()