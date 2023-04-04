from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),   
    path('games/', views.games),
    path('games/wakfu/', views.wakfu),
]
