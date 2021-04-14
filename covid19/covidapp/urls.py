
from django.urls import path
from .views import helloworldviews

urlpatterns = [
    path('',helloworldviews),
]