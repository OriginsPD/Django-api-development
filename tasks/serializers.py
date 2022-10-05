from rest_framework import serializers
from tasks.models import *
from comments.serializers import *


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    subject = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'author', 'subject')

    depth = 2
