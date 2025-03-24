from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('fetch-characters/', views.fetch_characters, name='fetch-characters'),
    path('characters/', views.character_list, name='character-list'),
    path('characters/create/', views.character_create, name='character-create'),
    path('characters/update/<int:pk>/', views.character_update, name='character-update'),
    path('characters/delete/<int:pk>/', views.character_delete, name='character-delete'),
    path('locations/', views.location_list, name='location-list'),
    path('locations/create/', views.location_create, name='location-create'),
    path('locations/update/<int:pk>/', views.location_update, name='location-update'),
    path('locations/delete/<int:pk>/', views.location_delete, name='location-delete'),
]
