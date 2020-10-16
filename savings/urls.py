from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('aim-list', views.aim_list, name="aim-list"),
    path('aim-create', views.aim_create, name="aim-create"),
    path('aim-update/<str:pk>/', views.aim_update, name="aim-update"),
    path('aim-delete/<str:pk>/', views.aim_delete, name="aim-delete"),
]
