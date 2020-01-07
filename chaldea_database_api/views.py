from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Servant, Class
from .serializer import ServantSerializer, ClassSerializer


# Create your views here.
class ServantViewSet(viewsets.ModelViewSet):
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
