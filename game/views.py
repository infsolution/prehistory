from rest_framework import status, generics, serializers
from rest_framework import permissions
from django_filters import rest_framework as filters
from django.shortcuts import render
from game.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated),
    name = 'user-detail'

class AvatarList(generics.ListCreateAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    #permission_classes = (permissions.IsAuthenticated),
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    name = 'avatar-list'

class AvatarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = (permissions.IsAuthenticated),
    name = 'avatar-detail'


class KnowingList(generics.ListCreateAPIView):
    queryset = Knowing.objects.all()
    serializer_class = KnowingSerializer
    #permission_classes = (permissions.IsAuthenticated),
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    name = 'knowing-list'

class KnowingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knowing.objects.all()
    serializer_class = KnowingSerializer
    permission_classes = (permissions.IsAuthenticated),
    name = 'knowing-detail'

class AvatarKnowingList(generics.ListCreateAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarKnowingSerializer
    permission_classes = (permissions.IsAuthenticated),
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    name = 'avatarknowing-list'

class AvatarKnowingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarKnowingSerializer
    permission_classes = (permissions.IsAuthenticated),
    name = 'avatarknowing-detail'

class AvatarItemList(generics.ListCreateAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarItemSerializer
    permission_classes = (permissions.IsAuthenticated),
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    name = 'avataritem-list'

class AvatarItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarItemSerializer
    permission_classes = (permissions.IsAuthenticated),
    name = 'avataritem-detail'