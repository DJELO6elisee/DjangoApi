from django.shortcuts import render  # Permet de gérer les réponses basées sur des templates (non utilisé ici)
from product.serializer import ProductSerializer  # Importation du serializer pour les produits (non utilisé ici)
from rest_framework import generics  # Classes génériques pour créer des vues
from rest_framework.response import Response  # Pour envoyer des réponses HTTP personnalisées

from . import client  # Importation du module client pour effectuer la recherche personnalisée

# ------------------------------------------------------
# Classe pour gérer les recherches et retourner les résultats correspondants
# ------------------------------------------------------
class SearchListView(generics.ListAPIView):
    """
    Vue pour effectuer une recherche personnalisée.

    - La recherche est effectuée via une méthode dans le module `client`.
    - Les résultats dépendent des paramètres envoyés dans la requête.
    - Si aucun paramètre `query` (`q`) n'est fourni, une réponse avec un statut 404 est retournée.
    """

    def get(self, request, *args, **kwargs):
        """
        Méthode pour gérer les requêtes GET.

        - Vérifie si l'utilisateur est authentifié.
        - Lit les paramètres `public`, `tag` et `q` dans l'URL.
        - Envoie la requête à une méthode client pour effectuer la recherche.
        - Retourne les résultats ou un message d'erreur si aucun résultat n'est trouvé.
        """
        user = None
        if request.user.is_authenticated:  # Vérifie si l'utilisateur est connecté
            user = request.user.username  # Récupère le nom d'utilisateur

        # Récupération des paramètres de la requête
        public = str(request.GET.get('public')) != "0"  # Définit si la recherche est publique ou privée
        tag = request.GET.get('tag')  # Récupère le tag (facultatif)
        query = request.GET.get('q')  # Récupère la requête de recherche (obligatoire)

        # Si aucun terme de recherche n'est fourni, retourne une erreur 404
        if not query:
            return Response("pas trouvé", status=404)

        # Effectue la recherche en appelant une fonction dans le module client
        result = client.perform_search(query, user=user, public=public, tags=tag)

        # Retourne les résultats au format JSON
        return Response(result)
