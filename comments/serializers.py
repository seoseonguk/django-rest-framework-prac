from django.contrib.auth import get_user_model

from rest_framework import serializers, viewsets

from .models import Comment

User = get_user_model()

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Comment
        fields = [
            'url',
            'id',
            'parent',
            'user',
            'text'
        ]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer