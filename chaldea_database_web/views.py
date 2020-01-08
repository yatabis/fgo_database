from django.shortcuts import render
from django.views.generic import ListView

from chaldea_database_api.models import Servant


# Create your views here.
class ServantsListView(ListView):
    model = Servant
    template_name = 'chaldea_database_web/servants.html'
    context_object_name = 'servants_list'


class SynthesisListView(ListView):
    model = Servant
    template_name = 'chaldea_database_web/synthesis.html'
    context_object_name = 'servants_list'
