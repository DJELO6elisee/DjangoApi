from .models import Product
from.serializer import ProductSerializer, UserSerializer

from rest_framework import viewsets
from django.contrib.auth.models import User



class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


