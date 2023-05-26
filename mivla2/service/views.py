from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from services.permissions import *
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .serializers import SofaSerializer, WardrobeSerializer, StolSerializer, FurnitureSerializer, OrdersSerializer, \
    LoginSerializer, UserSerializer, LogoutSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView


def filtre_universale(parameter_dict: dict):
    str_for_return = ''
    for key, value in parameter_dict.items():
        str_for_return += f"{key}={value},"
    return str_for_return[:len(str_for_return)-1]


def shop(request):
    product = Service()
    lister = product.get_all(Sofa, Wardrobe, Stol)
    context = {'items': lister}
    return render(request, 'services/catalog.html', context)


class Service:
    def get_all(self, *args):
        list_of_all_obj = [i.objects.all() for i in args]
        return list_of_all_obj

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)

class SofaViewSet(viewsets.ModelViewSet):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StolViewSet(viewsets.ModelViewSet):
    queryset = Stol.objects.all()
    serializer_class = StolSerializer
    permission_classes = (IsAdminOrReadOnly,)


class WardrobeViewSet(viewsets.ModelViewSet):
    queryset = Wardrobe.objects.all()
    serializer_class = WardrobeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = (IsAdminOrReadOnly,)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, )


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
