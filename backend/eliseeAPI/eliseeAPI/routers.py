from rest_framework.routers import DefaultRouter
from product.views_set import ProductViewset, UserViewSet  # Assurez-vous que les importations sont correctes

# Créez un seul routeur
router = DefaultRouter()

# Enregistrez les ViewSets dans le même routeur
router.register('product', ProductViewset, basename='product')
router.register(r'users', UserViewSet, basename='user')

# Cette ligne définit les URLs du routeur dans urlpatterns
urlpatterns = router.urls  # Enregistrez toutes les URLs générées par le routeur

# Vous n'avez pas besoin de redéclarer le routeur ici, car il a déjà été configuré au-dessus.
