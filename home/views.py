from django.shortcuts import render, get_object_or_404
from wagtail.models import Page

def home_view(request):
    home_page = get_object_or_404(Page, slug='inicio')
    return render(request, 'home/home_page.html', {
        'page': home_page,
    })