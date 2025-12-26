# properties/views.py

from django.shortcuts import render, get_object_or_404
from .models import PropertyIndexPage, PropertyPage  # Use your actual model names

def property_index_view(request):
    property_index_page = get_object_or_404(PropertyIndexPage, slug='imóveis')
    properties = PropertyPage.objects.all()  # Adjust queryset as needed
    return render(request, 'properties/property_index_page.html', {
        'page': property_index_page,
        'properties': properties,
    })
