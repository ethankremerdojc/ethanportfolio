
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('squareteroids/', include('squareteroids.urls')),
    path('admin/', admin.site.urls),
]
