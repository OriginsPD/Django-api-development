from django.urls import path
from comments.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', CommentsList.as_view()),
    path('<int:pk>/', CommentsDetail.as_view(), name="comments-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
