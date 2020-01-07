from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Servant, Class
from .serializer import ServantSerializer, ClassSerializer


# Create your views here.
class ServantFilter(django_filters.FilterSet):
    class_name = django_filters.CharFilter(field_name='class_name__name')

    class Meta:
        model = Servant
        fields = ['class_name', 'rarity']


class ServantViewSet(viewsets.ModelViewSet):
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer
    filter_class = ServantFilter


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
