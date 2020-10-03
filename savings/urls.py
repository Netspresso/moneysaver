from django.urls import path
from .views import all_aims, new_aim, edit_aim, delete_aim

urlpatterns = [
    path('all/', all_aims, name='all_aims'),
    path('new/', new_aim, name='new_aim'),
    path('edit/<int:id>/', edit_aim, name='edit_aim'),
    path('delete/<int:id>/', delete_aim, name='delete_aim'),
]