from rest_framework import serializers
from blogs import models


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    blog = serializers.CharField()


class BlogModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = models.Blog
        fields = ('id', 'title', 'body')
