from django.contrib import admin
from django.urls import path, include #with the help of include we can use the urls for navigation in baseline urls in root directory.
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
]
