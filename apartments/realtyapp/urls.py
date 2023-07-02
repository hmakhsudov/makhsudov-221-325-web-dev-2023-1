from django.urls import path
from .views import index, garages, new_buildings, favorites, purchases, houses, apartment, apartment_test, add_to_favorites, delete_from_favorites, add_to_purchases

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('garages/', garages, name='garages'),
    path('new_buildings/', new_buildings, name='new_buildings'),
    path('favorites/', favorites, name='favorites'),
    path('purchases/', purchases, name='purchases'),
    path('houses/', houses, name='houses'),
    path('apartment/<int:id>/', apartment, name='apartment'),
    path('add_to_favorites/<int:id>/', add_to_favorites, name='add_to_favorites'),
    path('add_to_purchases/<int:id>/', add_to_purchases, name='add_to_purchases'),
    path('delete_from_favorites/<int:id>/', delete_from_favorites, name='delete_from_favorites'),
    path('apartment_test/', apartment_test, name='apartment_test')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)