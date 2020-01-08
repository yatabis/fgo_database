from django.urls import path
from .views import ServantsListView

urlpatterns = [
    path('spirit-origin', ServantsListView.as_view(), name='servants'),
]
