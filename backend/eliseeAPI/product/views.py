from .models import Product  # Importation du modèle Product
from rest_framework.response import Response  # Utilisé pour envoyer une réponse HTTP
from .serializer import ProductSerializer  # Importation du serializer pour le modèle Product
from rest_framework import generics, mixins, permissions  # Outils DRF pour créer des vues génériques et gérer les permissions
from .permissions import IsStaffPerm  # Permission personnalisée (vérification du rôle staff)

# ------------------------------------------------------
# Classe pour afficher les détails d'un produit spécifique
# ------------------------------------------------------
class DetailApiView(generics.RetrieveAPIView):
    """
    Vue pour récupérer les détails d'un produit en fonction de son ID.
    """
    queryset = Product.objects.all()  # Ensemble de données à utiliser
    serializer_class = ProductSerializer  # Serializer pour transformer les objets en JSON

# ------------------------------------------------------
# Classe pour créer un produit
# ------------------------------------------------------
class CeateApiView(generics.CreateAPIView):
    """
    Vue pour créer un nouveau produit.
    """
    queryset = Product.objects.all()  # Ensemble de données (non utilisé ici pour la création)
    serializer_class = ProductSerializer  # Serializer pour valider et sauvegarder les données

# ------------------------------------------------------
# Classe pour mettre à jour un produit
# ------------------------------------------------------
class UpdateProductView(generics.UpdateAPIView):
    """
    Vue pour mettre à jour un produit existant.
    """
    queryset = Product.objects.all()  # Ensemble de données à utiliser
    serializer_class = ProductSerializer  # Serializer pour valider et appliquer les modifications
    lookup_field = 'id'  # Champ utilisé pour identifier l'objet à mettre à jour

# ------------------------------------------------------
# Classe pour supprimer un produit
# ------------------------------------------------------
class DeleteProductView(generics.DestroyAPIView):
    """
    Vue pour supprimer un produit en fonction de son ID.
    """
    queryset = Product.objects.all()  # Ensemble de données à utiliser
    serializer_class = ProductSerializer  # Serializer utilisé (non obligatoire pour une suppression)
    lookup_field = 'id'  # Champ utilisé pour identifier l'objet à supprimer

# ------------------------------------------------------
# Classe pour lister et créer des produits
# ------------------------------------------------------
class ListCreateApiView(generics.ListCreateAPIView):
    """
    Vue pour lister tous les produits et en créer de nouveaux.
    - Nécessite que l'utilisateur soit un administrateur ou un membre du staff.
    """
    permission_classes = [permissions.IsAdminUser, IsStaffPerm]  # Permissions nécessaires pour accéder à cette vue
    queryset = Product.objects.all()  # Ensemble de données à afficher
    serializer_class = ProductSerializer  # Serializer utilisé pour la liste et la création

# ------------------------------------------------------
# Classe pour afficher une liste de produits
# ------------------------------------------------------
class ListProductApiView(generics.ListAPIView):
    """
    Vue pour récupérer une liste de tous les produits disponibles.
    """
    queryset = Product.objects.all()  # Ensemble de données à afficher
    serializer_class = ProductSerializer  # Serializer pour transformer les objets en JSON

# ------------------------------------------------------
# Vue basée sur des mixins pour gérer plusieurs actions sur les produits
# ------------------------------------------------------
# class ProductMixinsView(
#     generics.GenericAPIView, 
#     mixins.CreateModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.ListModelMixin, 
#     mixins.DestroyModelMixin, 
#     mixins.RetrieveModelMixin
# ):
#     """
    # Vue générique utilisant des mixins pour gérer plusieurs opérations :
    # - Création
    # - Mise à jour
    # - Liste
    # - Suppression
    # - Détails (Retrieve)
    # """
    # queryset = Product.objects.all()  # Ensemble de données à utiliser
    # serializer_class = ProductSerializer  # Serializer pour toutes les opérations

    # Vous pouvez définir des méthodes supplémentaires pour chaque action si nécessaire.
