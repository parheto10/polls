from django.urls import path
from .views import home, ajouter, vote, results


urlpatterns = [
    path('', home, name="home"),
    path('ajouter/', ajouter, name="ajouter"),
    path('vote/<int:id>', vote, name="vote"),
    path('resultats/<int:id>', results, name="results"),
]