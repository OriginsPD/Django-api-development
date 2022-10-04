from django.urls import path
from tasks.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', TasksList.as_view()),
    path('<int:pk>/', TasksDetail.as_view(), name="tasks-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
