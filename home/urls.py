from django.urls import path
from .views import home_view

urlpatterns = [
    path('inicio/', home_view, name='home_page'),
]
