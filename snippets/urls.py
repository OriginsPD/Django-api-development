from django.urls import path
from snippets.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name="snippet-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
