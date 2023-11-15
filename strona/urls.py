from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('posty/', views.posty, name='posty'),
    path('nauka/', views.nauka, name='nauka'),
    path('kontakt/', views.kontakt, name='kontakt'),
]
