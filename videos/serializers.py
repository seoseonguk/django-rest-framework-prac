#전부 rest_framework에서 온다.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from comments.serializers import CommentSerializer
from .models import Video, Category



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'url',
            'id',
            'slug',
            'title',
            'description',
            'image'
        ]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#JSON Serializer로 만드는 부분
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    # category_title = serializers.CharField(source='category.title', read_only=True)
    # category_image = serializers.CharField(source='category.get_image_url', read_only=True)
    #  미리 정의된 method가 있어야한다.
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
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
            'category',
            # 'category_title',
            # 'category_image',
            'comment_set'
        ]


#Viewset - url에 연결
class VideoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
