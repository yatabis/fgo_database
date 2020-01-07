from rest_framework import serializers

from .models import Servant, Class


class ServantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servant
        fields = ('number', 'name', 'class_name', 'rarity')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('name',)
