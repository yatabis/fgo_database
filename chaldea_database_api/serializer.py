from rest_framework import serializers

from .models import Servant, Class


class ServantSerializer(serializers.ModelSerializer):
    class_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Servant
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
