from rest_framework import serializers
from comments.models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    subject = serializers.ReadOnlyField(source='tasks.title',)

    class Meta:
        model = Comments
        fields = ('id', 'content', 'subject', 'author')
