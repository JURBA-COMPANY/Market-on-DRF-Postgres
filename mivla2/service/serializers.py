from rest_framework import serializers
from mivla2.service.models import Furniture


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ('length', 'height', 'depth', 'ship', 'colour')


class SofaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ('self_id', 'fur', 'num_seats', 'expand', 'corner')


class StolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ('self_id', 'fur', 'expand')


class WardrobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ('self_id', 'fur', 'num_shelfs')
