from django.http import Http404, JsonResponse
from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from poissonerieapp.config import baseUrl
from poissonerieapp.models import *
from poissonerieapp.serializers import *


# Create your views here.

class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl + 'products/')
        jsondata = response.json()

        # Dictionnaire de correspondance entre l'ID de la catégorie et son nom
        # categories_mapping = {
        #     0: "poisson de mer",
        #     1: "crustacés",
        #     2: "fruit de mer"
        # }

        # Parcours des données JSON et enregistrement dans la base de données
        for produit_json in jsondata:

            # categorie_id = produit_json['category'],
            #
            # # Vérification du type de categorie_id
            # if isinstance(categorie_id, tuple):
            #     categorie_id = categorie_id[0]
            #
            # # Vérification si l'ID de catégorie est dans le dictionnaire
            # if categorie_id in categories_mapping:
            #     categorie_nom = categories_mapping[categorie_id]
            # else:
            #     categorie_nom = "Autres"
            #
            # categorie_nom = categories_mapping.get(categorie_id, categorie_nom)
            #
            # # Création d'une instance de CategorieProduit
            # categorie = CategorieProduit.objects.create(value=categorie_id, nom=categorie_nom)

            # Création d'une instance de Produit avec les données JSON
            produit = Produit.objects.create(
                id=produit_json['id'],
                name=produit_json['name'],
                category=produit_json['category'],
                price=produit_json['price'],
                unit=produit_json['unit'],
                availability=produit_json['availability'],
                sale=produit_json['sale'],
                discount=produit_json['discount'],
                comments=produit_json['comments'],
                owner=produit_json['owner'],
            )

        return Response("Produits enregistrés avec succès dans la base de données.")


class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404


class PromoList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)


#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
        jsondata = response.json()
        return Response(jsondata)


class RedirectionListDeShipPoints(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl + 'shipPoints/')
        jsondata = response.json()
        return Response(jsondata)


class RedirectionDetailShipPoint(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl + 'shipPoint/' + str(pk) + '/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404


class ProductAvailableList(APIView):
    def get(self, request, format=None):
        res = []
        for prod in ProduitValid.objects.all():
            serializer = ProduitValidSerializer(prod)
            response = requests.get(baseUrl + 'availableproducts/' + str(serializer.data['tigID']) + '/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def produit_list(request):
    if request.method == 'GET':
        produits = Produit.objects.all()
        produits_serializer = ProduitSerializer(produits, many=True)
        return Response(produits_serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def produit_detail(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response({'Error': 'Produit not found'})
    if request.method =='GET':
        produit_serializer = ProduitSerializer(produit)
        return Response(produit_serializer.data)


@api_view(['PUT'])
def produit_update_discount(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response({'Error': 'Produit not found'}, status=404)

    if request.method == 'PUT':
        discount = request.data.get('discount')
        if discount is not None:
            produit.discount = discount
            produit.save()
            return Response({'message': 'Discount updated successfully'})
        else:
            return Response({'Error': 'Discount not provided'}, status=400)


@api_view(['PUT'])
def produit_update_stock(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response({'Error': 'Produit not found'}, status=404)

    if request.method == 'PUT':
        stock = request.data.get('stock')
        if stock is not None:
            produit.stock = stock
            produit.save()
            return Response({'message': 'Stock updated successfully'})
        else:
            return Response({'Error': 'Stock not provided'}, status=400)


@api_view(['PUT'])
def produits_update(request):
    if request.method == 'PUT':
        data = request.data
        errors = []

        for item in data:
            produit_id = item.get('id')
            produit_data = {
                'discount': item.get('discount'),
                'stock': item.get('stock')
            }
            try:
                produit = Produit.objects.get(pk=produit_id)
                serializer = ProduitSerializer(produit, data=produit_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    errors.append(serializer.errors)
            except Produit.DoesNotExist:
                errors.append({'id': produit_id, 'error': 'Produit not found'})

        if errors:
            return Response({'errors': errors}, status=400)
        else:
            return Response({'message': 'Tous les produits ont été mis à jour'})
    else:
        return Response({'Error': 'Méthode non autorisée'}, status=405)        