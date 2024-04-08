from django.urls import path
from . import views

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('posty/', views.posty, name='posty'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('wiecej/', views.wiecej, name='wiecej'),
]
