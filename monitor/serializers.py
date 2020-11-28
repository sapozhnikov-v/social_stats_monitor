from rest_framework import serializers
from .models import Source, Stat


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = 'id', 'name', 'link', 'internal_id', 'type_social', 'avatar'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = 'id', 'count_subscribers', 'updated_at', 'source'

    source = SourceSerializer
