from django.contrib import admin
from .models import Produit, Categorie, Utilisateur, Ticket, Stock, Fournisseur

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'description')
    search_fields = ('nom', 'description')
    list_filter = ('categorie',)

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age', 'tel', 'mail', 'role')
    search_fields = ('nom', 'prenom', 'mail')
    list_filter = ('role',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('reference', 'nombre', 'produit', 'date')
    search_fields = ('reference', 'produit__nom')
    list_filter = ('date', 'produit')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'nombre')
    search_fields = ('produit__nom',)

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numero_tel', 'email')
    search_fields = ('nom', 'prenom', 'email')
