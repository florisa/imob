from django.shortcuts import render, get_object_or_404
from wagtail.models import Page

def contact_view(request):
    contact_page = get_object_or_404(Page, slug='contato')
    return render(request, 'contact/contact_page.html', {
        'page': contact_page,
    })