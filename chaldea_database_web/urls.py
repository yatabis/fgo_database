from django.urls import path
from .views import ServantsListView, SynthesisListView

urlpatterns = [
    path('spirit-origin', ServantsListView.as_view(), name='servants'),
    path('synthesis-scheme', SynthesisListView.as_view(), name='synthesis'),
]
