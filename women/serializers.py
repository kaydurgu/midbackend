import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from women.models import Women, Category


# class WomenModel:
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance


class CaregorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
