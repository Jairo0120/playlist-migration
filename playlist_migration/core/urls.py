from django.urls import path
from core.views import TestView

urlpatterns = [
    path('test/', TestView.as_view())
]