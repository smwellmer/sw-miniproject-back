from .models import List
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model that will serialize
        model = List
        # the field that should be included in the serializer output.
        fields = ['id', 'item', 'list']