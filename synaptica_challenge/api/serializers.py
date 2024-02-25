from rest_framework import serializers
from synaptica_challenge.api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'description'
        ]
