#전부 rest_framework에서 온다.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from comments.serializers import CommentSerializer
from .models import Video, Category


# HyperlinkedIdentityField

class VideoUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'cat_slug': obj.category.slug,
            'vid_slug': obj.slug
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)


#JSON Serializer로 만드는 부분
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    url = VideoUrlHyperlinkedIdentityField('video_detail_api')
    # category = CategorySerializer(many=False, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    category_url = serializers.CharField(source='category.get_absolute_url', read_only=True)
    #  미리 정의된 method가 있어야한다.
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Video
        # 여기에 추가된것들이 JSON으로 전달된다.
        fields = [
            'url',
            'id',
            'slug',
            'title',
            'order',
            'embed_code',
            'free_preview',
            'share_message',
            'timestamp',
            'category_url',
            'comment_set'
        ]


#Viewset - url에 연결
class VideoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class CategoryUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    # lookup_field = 'slug'

    def get_url(self, obj, view_name, request, format):
        kwargs = {
            'slug': obj.slug
        }
        return reverse(view_name, kwargs=kwargs, request=request, format=format)



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # url = CategoryUrlHyperlinkedIdentityField(view_name='category_detail_api')
    url = CategoryUrlHyperlinkedIdentityField('category_detail_api', lookup_field='slug')

    video_set = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'url',
            'id',
            'slug',
            'title',
            'description',
            'image',
            'video_set',
        ]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

