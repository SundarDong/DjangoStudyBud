from django.urls import path
from . import views #we use . because the view py file is in the main base app.

urlpatterns = [
    path('',views.home, name='home'),
    path('room/<str:pk>/',views.room, name='room'),
]
