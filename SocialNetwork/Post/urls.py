from django.urls import path, include
from Post.views import *

urlpatterns = [
    path('create', PostCreateView.as_view()),
    path('<int:pk>/like', LikeCreateView.as_view()),
    path('<int:pk>/unlike', LikeDeleteView.as_view()),
    path('list', PostListView.as_view()),
    path('like/list', LikeListView.as_view()),

]
