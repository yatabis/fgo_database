from django.urls import path
from .views import ServantsListView

urlpatterns = [
    path('servants', ServantsListView.as_view(), name='servants'),
]
