from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.squareteroids, name='game'),
    path('post', views.post_score, name='post_score')
]

# urlpatterns += static(
#     "static", 
#     document_root=settings.STATIC_ROOT + "/squareteroids"
# )