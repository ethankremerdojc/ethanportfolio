from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.squareteroids, name='game'),
    path('start', views.start_time, name='start_time'),
    path('end', views.end_time, name='end_time'),
]