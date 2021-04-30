from rest_framework import serializers
from .models import CustomUser


class UserDetailserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('last_login', )