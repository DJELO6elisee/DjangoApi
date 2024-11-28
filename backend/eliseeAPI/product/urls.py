from django.urls import path
from .views import DetailApiView, CeateApiView, UpdateProductView, DeleteProductView, ListCreateApiView, ListProductApiView
from rest_framework.authtoken.views import obtain_auth_token

# , ProductMixinsView

urlpatterns = [
    # Routes pour les vues personnalisées
    path('detail/<int:id>/', DetailApiView.as_view(), name='product-detail'),
    path('update/<int:id>/', UpdateProductView.as_view(), name='product-update'),
    path('create/', CeateApiView.as_view(), name='product-create'),
    path('listcreate/', ListCreateApiView.as_view(), name='product-listcreate'),
    path('list/', ListProductApiView.as_view(), name='product-list'),
    path('delete/<int:id>/', DeleteProductView.as_view(), name='product-delete'),

    
    # Authentification DRF
    path('auth/', obtain_auth_token, name='api-token-auth'),

    # Routes mixins commentées si nécessaire
    # path('mixins/', ProductMixinsView.as_view()),
    # path('detail/<int:pk>/', ProductMixinsView.as_view()),
    # path('update/<int:pk>/', ProductMixinsView.as_view()),
    # path('delete/<int:pk>/', ProductMixinsView.as_view()),
    # path('create/', ProductMixinsView.as_view()),
    # path('list/', ProductMixinsView.as_view()),
]
