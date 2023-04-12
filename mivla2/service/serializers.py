from rest_framework import serializers
from .models import *


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ('length', 'height', 'depth', 'ship', 'colour')


class SofaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sofa
        fields = ('self_id', 'fur', 'num_seats', 'expand', 'corner')


class StolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stol
        fields = ('self_id', 'fur', 'expand')


class WardrobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wardrobe
        fields = ('self_id', 'fur', 'num_shelfs')
