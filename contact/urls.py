from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contato/', contact_view, name='contact_page'),
]
