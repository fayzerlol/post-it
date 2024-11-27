from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_postit.urls')),  # Inclui as URLs do app_postit
]
