from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', RoomView.as_view())
]
