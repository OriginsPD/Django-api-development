from rest_framework import serializers
from tasks.models import *


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'author')
