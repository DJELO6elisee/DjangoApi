from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User

from .models import Product

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'}  # Corrigez la vue ici
        }


class ProductSerializer(HyperlinkedModelSerializer):
    # user_name = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',  # Vue associée au modèle User
    #     queryset=User.objects.all()
    # )

    user_name = serializers.CharField(source="user", read_only=True)

    class Meta:
        model = Product
        fields = ['user_name', 'url', 'name', 'content', 'price']  # Incluez 'url' pour les relations hyperliées
        extra_kwargs = {
            'url': {'view_name': 'product-detail', 'lookup_field': 'id'}  # Assurez-vous que cela correspond
        }


