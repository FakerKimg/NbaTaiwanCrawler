from rest_framework import serializers
from news.models import News

class NewsSerializer(serializers.Serializer):
    href = serializers.CharField(max_length=100)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    datetime = serializers.DateTimeField()
    content = serializers.CharField(required=False, max_length=1024)
    coverimg = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `News` instance, given the validated data.
        """
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `News` instance, given the validated data.
        """
        instance.href = validated_data.get('href', instance.href)
        instance.title = validated_data.get('title', instance.title)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.content = validated_data.get('content', instance.content)
        instance.coverimg = validated_data.get('coverimg', instance.title)
        instance.save()
        return instance


