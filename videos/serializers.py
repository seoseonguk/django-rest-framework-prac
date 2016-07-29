#전부 rest_framework에서 온다.

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from .models import Video


#JSON Serializer로 만드는 부분
class VideoSerializer(serializers.HyperlinkedModelSerializer):
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


#Viewset - url에 연결
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
