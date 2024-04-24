from django.urls import path

from poissonerieapp import views
from poissonerieapp.views import produit_list, produit_detail, produit_update_discount, produits_update, produit_update_stock

urlpatterns = [
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),
    path('shipPoints/', views.RedirectionListDeShipPoints.as_view()),
    path('shipPoint/<int:pk>', views.RedirectionDetailShipPoint.as_view()),
    path('availableproducts/', views.ProductAvailableList.as_view()),

    path('getAllProducts/', produit_list),
    path('getProduct/<int:pk>', produit_detail),
    path('updateDiscount/<int:pk>', produit_update_discount),
    path('updateStock/<int:pk>', produit_update_stock),
    path('updateAllProducts/', produits_update)
]
