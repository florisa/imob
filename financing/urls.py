from django.urls import path
from .views import financing_view

urlpatterns = [
    path('financiamento/', financing_view, name='financing_page'),
]
