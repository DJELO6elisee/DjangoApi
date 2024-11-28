from .models import Product  # Importation du modèle Product
from .serializer import ProductSerializer, UserSerializer  # Importation des serializers pour Product et User

from rest_framework import viewsets  # Importation des ViewSets pour créer rapidement des vues complètes
from django.contrib.auth.models import User  # Importation du modèle User de Django

# ------------------------------------------------------
# VueSet pour gérer toutes les opérations CRUD sur les produits
# ------------------------------------------------------
class ProductViewset(viewsets.ModelViewSet):
    """
    VueSet pour gérer les produits.

    - Permet de lister, créer, récupérer, mettre à jour et supprimer des produits.
    - Utilise `ProductSerializer` pour valider et sérialiser les données.
    """
    queryset = Product.objects.all()  # Ensemble de données pour les produits
    serializer_class = ProductSerializer  # Serializer utilisé pour les opérations
    lookup_field = 'id'  # Champ utilisé pour identifier les produits (par défaut : `pk`)

# ------------------------------------------------------
# VueSet pour gérer les utilisateurs
# ------------------------------------------------------
class UserViewSet(viewsets.ModelViewSet):
    """
    VueSet pour gérer les utilisateurs.

    - Permet de lister, créer, récupérer, mettre à jour et supprimer des utilisateurs.
    - Utilise `UserSerializer` pour valider et sérialiser les données utilisateur.
    - Basé sur le modèle utilisateur par défaut de Django.
    """
    queryset = User.objects.all()  # Ensemble de données pour les utilisateurs
    serializer_class = UserSerializer  # Serializer utilisé pour les opérations
    lookup_field = 'id'
    
