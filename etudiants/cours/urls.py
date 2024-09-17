from django.urls import path
from . import views
from .views import image_carousel

urlpatterns = [
    path('', views.home, name='home'),
    path('scientifique/', views.scientifique, name='scientifique'),
    path('scientifique/<str:departement_nom>/', views.departement, name='departement'),
    path('scientifique/<str:departement_nom>/<str:niveau_nom>/', views.niveau, name='niveau'),
    # Routes pour la partie littéraire
    path('litteraire/', views.litteraire, name='litteraire'),
    path('litteraire/<str:departement_nom>/', views.departement_litteraire, name='departement_litteraire'),
    path('litteraire/<str:departement_nom>/<str:niveau_nom>/', views.niveau_litteraire, name='niveau_litteraire'),
    path('carousel/', image_carousel, name='carousel'),

]
