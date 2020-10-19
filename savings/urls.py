from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter
from knox import views as knox_views
from .views import LoginAPI

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', api_overview, name="api-overview"),
    path('aim-list/', aim_list, name="aim-list"),
    path('<str:user>/aim-list/', user_aim_list, name="user_aim-list"),
    path('aim-create/', aim_create, name="aim-create"),
    path('aim-update/<str:pk>/', aim_update, name="aim-update"),
    path('aim-delete/<str:pk>/', aim_delete, name="aim-delete"),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
urlpatterns += router.urls