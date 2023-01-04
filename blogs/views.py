from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from blogs import services, serializers


class BlogViewSet(ModelViewSet):
    serializer_class = serializers.BlogModelSerializer
    blog_services: services.BlogServicesInterface = services.BlogServicesV1()

    def get_queryset(self):
        return self.blog_services.get_blogs()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.blog_services.create_blog(data=serializer.validated_data)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BlogViewSetV2(ViewSet):
    blog_services: services.BlogServicesInterface = services.BlogServicesV1()

    def list(self, request):
        queryset = self.blog_services.get_blogs()
        serializer = serializers.BlogModelSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.blog_services.get_blogs()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.BlogModelSerializer(user)

        return Response(serializer.data)