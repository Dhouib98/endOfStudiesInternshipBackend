from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='produits/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    ROLE_CHOICES = [
        ('responsable', 'Responsable'),
        ('vendeur', 'Vendeur'),
    ]

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    tel = models.CharField(max_length=15)  # Use a char field with validation
    mail = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.prenom} {self.nom}'

class Ticket(models.Model):
    reference = models.CharField(max_length=100)
    nombre = models.PositiveIntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reference

class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    nombre = models.PositiveIntegerField()

    def __str__(self):
        return f'Stock of {self.produit.nom}'

class Fournisseur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    numero_tel = models.CharField(max_length=15)  # Use a char field with validation
    email = models.EmailField()

    def __str__(self):
        return f'{self.prenom} {self.nom}'