from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from blogs import models, serializers, services


@api_view(['POST'])
def index(request):
    serializer = serializers.BlogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    blog = models.Blog.objects.create(**serializer.validated_data)

    serializer = serializers.BlogModelSerializer(blog)
    return Response(serializer.data)


class BlogAPIView(CreateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = serializers.BlogModelSerializer
    blog_services: services.BlogServicesInterface = services.BlogServicesV1()

    def get_queryset(self):
        return self.blog_services.get_blogs()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.blog_services.create_blog(data=serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.blog_services.delete_blog(blog=instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        queryset = models.Blog.objects.all()
        serializer = serializers.BlogModelSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.BlogModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        models.Blog.objects.create(**serializer.validated_data)

        return Response(serializer.data)