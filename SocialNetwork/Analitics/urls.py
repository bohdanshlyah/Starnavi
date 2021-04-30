from django.urls import path, include
from .views import LikesAnaliticView


urlpatterns = [
    path('', LikesAnaliticView.as_view()),
    path('?date_from=<date_from>&date_to=<date_to>', LikesAnaliticView.as_view()),
]
