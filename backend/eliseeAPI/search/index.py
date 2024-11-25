# index.py

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from product.models import Product

@register(Product)
class YourModelIndex(AlgoliaIndex):
    # should_index = "is_public"
    fields = ('user', 'name', 'content', 'price', 'public')

    tags = "get_tags_list"

settings = {
    'searchableAttributes':['name', 'content'],
    'attributeforFaceting':['user', 'public']
}
    # geo_field = 'location'
    # settings = {'searchableAttributes': ['name']}
    # index_name = 'my_index'

