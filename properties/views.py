from django.shortcuts import render, get_object_or_404
from wagtail.models import Page

def property_index_view(request):
    property_index_page = get_object_or_404(Page, slug='imóveis')
    # Add properties queryset if needed
    return render(request, 'properties/property_index_page.html', {
        'page': property_index_page,
        # 'properties': properties,  # if you use this in your template
    })
