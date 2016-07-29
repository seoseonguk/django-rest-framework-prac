#전부 rest_framework에서 온다.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Video, Category



class VideoSerializer(serializers.HyperlinkedModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    # category_url = serializers.CharField(source='category.get_absolute_url',read_only=True)
    category_image = serializers.CharField(source='category.get_image_url', read_only=True)
    #  미리 정의된 method가 있어야한다.
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Video
        # 여기에 추가된것들이 JSON으로 전달된다.
        fields = [
            'id',
            'slug',
            'title',
            'order',
            'embed_code',
            'share_message',
            'timestamp',
            'category_title',
            'category',
            'category_image',
            # 'category_url',
        ]

#JSON Serializer로 만드는 부분
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    # category_url = serializers.CharField(source='category.get_absolute_url',read_only=True)
    category_image = serializers.CharField(source='category.get_image_url', read_only=True)
    #  미리 정의된 method가 있어야한다.
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Video
        # 여기에 추가된것들이 JSON으로 전달된다.
        fields = [
            'id',
            'slug',
            'title',
            'order',
            'embed_code',
            'share_message',
            'timestamp',
            'category_title',
            'category',
            'category_image',
            # 'category_url',
        ]


#Viewset - url에 연결
class VideoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
