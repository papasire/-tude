from django.db import models

# Modèle pour les départements (Informatique, Mathématiques, etc.)
#class Departement(models.Model):
  #  nom = models.CharField(max_length=100)

 #   def __str__(self):
 #       return self.nom

class Departement(models.Model):
    nom = models.CharField(max_length=100)

    FACULTE_CHOICES = [
        ('scientifique', 'Faculté des Sciences'),
        ('litteraire', 'Faculté des Economies'),
    ]
    faculte = models.CharField(max_length=15, choices=FACULTE_CHOICES)

    def __str__(self):
        return f'{self.nom} ({self.get_faculte_display()})'



# Modèle pour les niveaux (Licence 1, Licence 2, Licence 3)
class Niveau(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nom} - {self.departement.nom}'

# Modèle pour les cours et exercices
class CoursExercice(models.Model):
    TYPE_CHOICES = [
        ('cours', 'Cours'),
        ('exercice', 'Exercice'),
    ]
    
    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='documents/')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.titre} ({self.type}) - {self.niveau.nom}'


    