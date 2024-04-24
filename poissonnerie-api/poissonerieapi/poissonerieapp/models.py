from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

# Table des Catégories de Produits
class CategorieProduit(models.Model):
    value = models.IntegerField(default=0)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# Table  Produits
class Produit(models.Model):

    name = models.CharField(max_length=100)
    category = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100, null=True)
    availability = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    comments = models.TextField(null=True)
    owner = models.CharField(max_length=100, null=True)
    stock = models.IntegerField(default=0)

    # nom = models.CharField(max_length=100)
    # prix = models.DecimalField(max_digits=10, decimal_places=2)
    # unite = models.CharField(max_length=100, null=True)
    # disponible = models.BooleanField(default=False)
    # prix_promo = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, blank=True)
    # pourcentage_promo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # quantite_stock = models.IntegerField(default=0)
    # nombre_articles_vendus = models.IntegerField(default=0)
    # commentaire = models.TextField()
    # categorie = models.ForeignKey(CategorieProduit, null=True, on_delete=models.CASCADE)


# # Table des Promotions
# class Promotion(models.Model):
#     produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     pourcentage_reduction = models.DecimalField(max_digits=5, decimal_places=2)


# Table des Utilisateurs
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom


# Table des Ventes
class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    date_vente = models.DateField(auto_now_add=True)


# Table des Transactions
class Transaction(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    type_transaction = models.CharField(max_length=50)  # Ajout, vente, péremption, etc.


# Table des KPIs
class KPI(models.Model):
    chiffre_affaires = models.DecimalField(max_digits=15, decimal_places=2)
    marge = models.DecimalField(max_digits=15, decimal_places=2)
    impot_societes = models.DecimalField(max_digits=15, decimal_places=2)
    trimestre = models.IntegerField()
    annee = models.IntegerField()


# Table des Alertes
class Alerte(models.Model):
    type_alerte = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)


class ProduitEnPromotion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)


class ProduitValid(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)
