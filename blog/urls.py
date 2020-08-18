from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Home', views.Home, name='Home'),
    path('league_stats', views.league_stats,name='league'),
    path('pre', views.pre,name='pre')
]