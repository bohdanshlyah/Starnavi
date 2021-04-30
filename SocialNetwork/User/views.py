from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import CustomUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailserializer

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class UserActivityView(generics.RetrieveAPIView):
    serializer_class = UserActivitySerializer
    queryset = CustomUser.objects.all()