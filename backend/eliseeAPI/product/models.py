from django.db import models
from django.contrib.auth.models import User
import random
# from django.conf import settings

# Create your models here.

# User = settings.AUTH_USER_MODEL

class Product(models.Model):
    TAGS_LIST = ['voiture', 'vetement', 'sac', 'elecctronique']
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    public = models.BooleanField(default=True)
    

    def __str__(self):
        return str(self.name)

    def is_public(self)  -> bool:
        return self.public
    
    def get_tags_list(self):
        return [random.choice(self.TAGS_LIST)]
    