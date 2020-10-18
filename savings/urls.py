from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', api_overview, name="api-overview"),
    path('aim-list', aim_list, name="aim-list"),
    path('aim-create', aim_create, name="aim-create"),
    path('aim-update/<str:pk>/', aim_update, name="aim-update"),
    path('aim-delete/<str:pk>/', aim_delete, name="aim-delete"),
    path('register/', RegisterAPI.as_view(), name='register'),
]
urlpatterns += router.urls