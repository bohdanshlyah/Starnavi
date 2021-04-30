from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('signup', UserCreateView.as_view()),
    path('activity/<int:pk>', UserActivityView.as_view()),
]



#path('api-token-auth/', obtain_auth_token, name='api_token_auth'),