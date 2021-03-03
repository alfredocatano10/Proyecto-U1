from django.urls import path
from .views import HomePage, ContenidoPage, AcercaDe

urlpatterns = [

    path('', HomePage.as_view(), name = 'Home'),
    path('Contenido', ContenidoPage.as_view(), name = 'Contenido'),
    path('Acerca', AcercaDe.as_view(), name = 'Acerca'),
]