from rest_framework import serializers
from comments.models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    subject = serializers.ReadOnlyField(source='tasks.title',)

    class Meta:
        model = Comments
        fields = ('id', 'content', 'subject', 'author')

    # def create(self, validated_data):
    #     subject_data = validated_data.pop('subject')
    #     subject_instance = Comments.objects.create(**subject_data)
    #     print(subject_instance)
    #     # profile_instance = Profile.objects.create(
    #     #     subject=subject_instance, **validated_data)
    #     return subject_instance
