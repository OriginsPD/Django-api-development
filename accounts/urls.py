from django.urls import path, include
from accounts.views import *


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()),
]
