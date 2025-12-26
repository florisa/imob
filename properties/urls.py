from django.urls import path
from .views import property_index_view

urlpatterns = [
    path('imóveis/', property_index_view, name='property_index_page'),
]
