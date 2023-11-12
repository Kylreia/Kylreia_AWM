# awmProject/urls.py
from django.urls import path, include

from .views import HotelUpdateRetrieveView, ListCreateGenericViews


urlpatterns = [
    path("hotels", ListCreateGenericViews.as_view()),
    path(
        "hotels/<str:pk>",
        HotelUpdateRetrieveView.as_view(),
    ),
]
