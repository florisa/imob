from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        from properties.models import PropertyPage
        context['featured_properties'] = PropertyPage.objects.live().filter(featured=True)[:3]
        return context
