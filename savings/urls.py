from django.urls import path
from .views import all_aims, new_aim, edit_aim, delete_aim
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all/', all_aims, name='all_aims'),
    path('new/', new_aim, name='new_aim'),
    path('edit/<int:id>/', edit_aim, name='edit_aim'),
    path('delete/<int:id>/', delete_aim, name='delete_aim'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
