
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('portfolio.urls')),
    path('squareteroids/', include('squareteroids.urls')),
    path('admin/', admin.site.urls),
]