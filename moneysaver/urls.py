from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static/
# from django.contrib.auth import views as auth_views
# from rest_framework import routers
# from savings.views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include('savings.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
