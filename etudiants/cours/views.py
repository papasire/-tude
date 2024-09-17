from django.shortcuts import render, get_object_or_404
from .models import Departement, Niveau, CoursExercice

def home(request):
    return render(request, 'home.html')

def scientifique(request):
    departements_scientifiques = Departement.objects.filter(faculte='scientifique')
    return render(request, 'scientifique.html', {'departements': departements_scientifiques})
    #departements = Departement.objects.all()
    #return render(request, 'scientifique.html', {'departements': departements})


# Vue pour afficher les niveaux d'un département spécifique
def departement(request, departement_nom):
    departement = get_object_or_404(Departement, nom=departement_nom)
    niveaux = Niveau.objects.filter(departement=departement)
    return render(request, 'departement.html', {'departement': departement, 'niveaux': niveaux})


# Vue pour afficher les cours et exercices d'un niveau spécifique
def niveau(request, departement_nom, niveau_nom):
    departement = get_object_or_404(Departement, nom=departement_nom)
    niveau = get_object_or_404(Niveau, nom=niveau_nom, departement=departement)
    cours_exercices = CoursExercice.objects.filter(niveau=niveau)
    return render(request, 'niveau.html', {'niveau': niveau, 'cours_exercices': cours_exercices})

def litteraire(request):
    departements_litteraires = Departement.objects.filter(faculte='litteraire')
    return render(request, 'litteraire.html', {'departements': departements_litteraires})
    #departements = Departement.objects.all()
    #return render(request, 'litteraire.html', {'departements': departements})

# Vue pour afficher les niveaux d'un département littéraire spécifique
def departement_litteraire(request, departement_nom):
    departement = get_object_or_404(Departement, nom=departement_nom)
    niveaux = Niveau.objects.filter(departement=departement)
    return render(request, 'departement_litteraire.html', {'departement': departement, 'niveaux': niveaux})

# Vue pour afficher les cours et exercices d'un niveau littéraire spécifique
def niveau_litteraire(request, departement_nom, niveau_nom):
    departement = get_object_or_404(Departement, nom=departement_nom)
    niveau = get_object_or_404(Niveau, nom=niveau_nom, departement=departement)
    cours_exercices = CoursExercice.objects.filter(niveau=niveau)
    return render(request, 'niveau_litteraire.html', {'niveau': niveau, 'cours_exercices': cours_exercices})



def image_carousel(request):
    images = [
        {'url': 'static/images/image1.png'},
        {'url': 'static/images/image2.png'},
        {'url': 'static/images/image3.png'}
    ]
    return render(request, 'carousel.html', {'images': images})

