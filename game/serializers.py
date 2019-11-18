from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('url','pk', 'username', 'email', 'password')

class AbiliitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Abiliity
		fields = ('url', 'pk', 'name','force', 'allowed_level')
class KnowingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Knowing
		fields = ('url', 'pk', 'name', 'defense', 'allowed_level')

class AvatarSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	knowledge = KnowingSerializer(many=True, read_only=True)
	abiliities = AbiliitySerializer(many=True, read_only=True)
	class Meta:
		model = Avatar
		fields = ('url','pk', 'owner', 'name', 'force', 'defense', 'life', 'level', 'abiliities', 'knowledge')
