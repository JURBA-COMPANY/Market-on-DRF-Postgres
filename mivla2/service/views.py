from django.shortcuts import render
from .parent import Service
from .models import *


def shop(request):
    product = Service()
    lister = product.get_all(Sofa, Wardrobe, Stol)
    context = {'items': lister}
    return render(request, 'service/catalog.html', context)


class SofaAPIView(generics.ListCreateAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer


class StolAPIView(generics.ListCreateAPIView):
    queryset = Stol.objects.all()
    serializer_class = StolSerializer


class WardrobeAPIView(generics.ListCreateAPIView):
    queryset = Wardrobe.objects.all()
    serializer_class = WardrobeSerializer
    
    
class FurnitureAPIView(generics.ListCreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class SofaEntityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer 
