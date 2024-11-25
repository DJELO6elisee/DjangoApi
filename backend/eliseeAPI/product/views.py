from .models import Product
# Create your views here.
# from django.http import JsonResponse
# from django.forms.models import model_to_dict

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework import generics, mixins, permissions, authentication
from .permissions import IsStaffPerm


# from .authentication import TokenAuthentication

# @api_view(['GET'])
class DetailApiView(generics.RetrieveAPIView):
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer

# @api_view(['POST'])
class CeateApiView(generics.CreateAPIView):
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductView(generics.UpdateAPIView):
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field= 'id'


class DeleteProductView(generics.DestroyAPIView):
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field= 'id'

class ListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser ,IsStaffPerm]
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer

    
class ListProductApiView(generics.ListAPIView):
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer

class ProductMixinsView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    queryset   = Product.objects.all()
    serializer_class = ProductSerializer


    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)
    
    # def perform_update(self, serializer):
    #     return super().perform_update(serializer)
    
    # def get(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     if pk is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    
    
