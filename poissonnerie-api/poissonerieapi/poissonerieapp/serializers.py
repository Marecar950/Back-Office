from rest_framework.serializers import ModelSerializer

from poissonerieapp.models import *


class CategorieProduitSerializer(ModelSerializer):
    class Meta:
        model = CategorieProduit
        fields = '__all__'


class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'


class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class VenteSerializer(ModelSerializer):
    class Meta:
        model = Vente
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class KPISerializer(ModelSerializer):
    class Meta:
        model = KPI
        fields = '__all__'


class AlerteSerializer(ModelSerializer):
    class Meta:
        model = Alerte
        fields = '__all__'


class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')


class ProduitValidSerializer(ModelSerializer):
    class Meta:
        model = ProduitValid
        fields = ('id', 'tigID')
