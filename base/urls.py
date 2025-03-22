from django.urls import path
from . import views #we use . because the view py file is in the main base app.

urlpatterns = [
    path('',views.home, name='home'),
    path('room/<str:pk>/',views.room, name='room'),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room")
]
