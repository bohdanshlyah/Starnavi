from django.shortcuts import render
from rest_framework import generics
from Post.models import Like
from .serializer import LikesAnaliticSerializer


class LikesAnaliticView(generics.ListAPIView):
    # date_from = '2021-04-28'
    # date_to = '2021-04-30'
    serializer_class = LikesAnaliticSerializer
    def get_queryset(self):
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        return Like.objects.filter(like_date__range=[date_from, date_to])
    