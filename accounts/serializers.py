from djoser.serializers import UserCreateSerializer
from accounts.models import *
from snippets.serializers import *
from tasks.serializers import *


class UserCreateSerializer(UserCreateSerializer):
    snippets = SnippetSerializer(
        many=True, read_only=True)

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'phone', 'snippets', 'tasks')
        depth = 2
