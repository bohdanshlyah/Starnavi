from rest_framework import serializers
from Post.models import Like


class LikesAnaliticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('__all__')
