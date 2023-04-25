from rest_framework import serializers
from .models import *



class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = ('colour_name',)
        
        
class FurnitureSerializer(serializers.ModelSerializer):
    
    colour = ColoursSerializer()
    
    class Meta:
        model = Furniture
        fields = ('length', 'height', 'depth', 'ship', 'colour')


class SofaSerializer(serializers.ModelSerializer):
    
    fur = FurnitureSerializer()
    
    class Meta:
        model = Sofa
        fields = ('self_id', 'fur', 'num_seats', 'expand', 'corner')


class StolSerializer(serializers.ModelSerializer):
    
    fur = FurnitureSerializer()
    
    class Meta:
        model = Stol
        fields = ('self_id', 'fur', 'expand')


class WardrobeSerializer(serializers.ModelSerializer):
    
    fur = FurnitureSerializer()
    
    class Meta:
        model = Wardrobe
        fields = ('self_id', 'fur', 'num_shelfs')
