from django.shortcuts import render, get_object_or_404
from wagtail.models import Page

def financing_view(request):
    financing_page = get_object_or_404(Page, slug='financiamento')
    return render(request, 'financing/financing_page.html', {
        'page': financing_page,
    })