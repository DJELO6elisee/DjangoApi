from django.urls import path
from .views import SearchListView

urlpatterns = [
    path('search_api/', SearchListView.as_view(), name="search"),
]
