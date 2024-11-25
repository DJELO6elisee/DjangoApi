from django.shortcuts import render
from product.serializer import ProductSerializer
from rest_framework import generics
from rest_framework.response import Response

from . import client
# Create your views here.
class SearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user =  None
        if request.user.is_authenticated:
            user = request.user.username
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag')
        query =  request.GET.get('q')
        if not query:
            return Response("pas trouvé", status = 404)
        
        result =  client.perform_search(query, user=user, public=public, tags=tag)
        return Response(result)
    