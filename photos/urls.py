from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.gallery,name = 'gallery'),
    path('photo/<str:pk>/',views.viewPhoto,name = 'photo'),
    path('add/',views.addPhoto,name = 'add'),
    path('location/<str:pk>/',views.location,name = 'location'),
]