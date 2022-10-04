from djoser.serializers import UserSerializer
from rest_framework import generics
from accounts.models import *
from accounts.serializers import *


# Create your views here.,

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
