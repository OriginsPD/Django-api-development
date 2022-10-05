from rest_framework import generics
from rest_framework import permissions
from comments.models import *
from tasks.models import *
from comments.serializers import *
# Create your views here.


class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        subject_data = self.request.data
        task = Tasks.objects.get(id=subject_data['subject'])
        serializer.save(subject=task, author=self.request.user)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
