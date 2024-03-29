import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from women.models import Women



#class WomenModel:
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
