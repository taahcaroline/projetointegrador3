from django.urls import path
from fakenewsapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.noticiascad, name='cadastro'),
    path('noticias/', views.buscar, name='buscar'),
    path('cadastradas/', views.noticiascadastradas, name='cadastradas'),
]