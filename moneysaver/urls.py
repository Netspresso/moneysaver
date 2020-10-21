from django.contrib import admin
from django.urls import path, include
from .views import api_overview

urlpatterns = [
    path('api/', include('savings.urls')),
    path('admin/', admin.site.urls),
    path('', api_overview, name='api-overview'),
]
