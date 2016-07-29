#전부 rest_framework에서 온다.

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from .models import Video


class VideoSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'slug',
            'title',
            'order',
            'embed_code',
            'share_message',
            'timestamp',
        ]