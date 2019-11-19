from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('url','pk', 'username', 'email', 'password')

class KnowingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Knowing
		fields = ('url', 'pk', 'name', 'force', 'defense', 'allowed_level')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('url', 'pk', 'name', 'force', 'defense', 'allowed_level')

class AvatarSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	knowing = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
	item = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
	class Meta:
		model = Avatar
		fields = ('url','pk', 'owner', 'name', 'force', 'defense', 'life', 'level', 'knowing', 'item')

class AvatarKnowingSerializer(serializers.HyperlinkedModelSerializer):
	knowing = serializers.SlugRelatedField(queryset=Knowing.objects.all(), many=True, slug_field='name')
	class Meta:
		model = Avatar
		fields = ('url', 'pk','knowing')

class AvatarItemSerializer(serializers.HyperlinkedModelSerializer):
	item = serializers.SlugRelatedField(queryset=Item.objects.all(), many=True, slug_field='name')
	class Meta:
		model = Avatar
		fields = ('url', 'pk','item')