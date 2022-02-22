from django.db import models
from django.urls import reverse

# Create your models here.
class Utilisateur(models.Model):
    pass

class Super(models.Model):
    intitulet = models.CharField(max_length=200)
    id_utilisateur= models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='product_magasin')
    file = models.FileField(upload_to='files')

    class Meta:
        abstract = True
        ordering = ['name']


class Epreuve(Super):
    matiere = models.CharField(max_length=200)
    filiere = models.CharField(max_length=200)
    professeur = models.CharField(max_length=200)

    
    def get_url(self):
        return reverse(kwargs={'pk':self.id})
    

class Correction(Super):
    id_epreuve= models.OneToOneField(Epreuve, on_delete=models.CASCADE, related_name="magasin_profil")
    def get_url(self):
        return reverse(kwargs={'pk':self.id})