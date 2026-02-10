from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('stats/', views.stats, name='stats'),
    path('<str:cca3>/', views.country_detail, name='country_detail'),
]
