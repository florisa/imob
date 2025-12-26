from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index


class PropertyIndexPage(Page):
    """Listagem de imóveis"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
    
    subpage_types = ['PropertyPage']
    parent_page_types = ['home.HomePage'] 
    
    def get_context(self, request):
        context = super().get_context(request)
        context['properties'] = PropertyPage.objects.child_of(self).live()
        return context


class PropertyPage(Page):
    """Imóvel individual"""
    
    reference = models.CharField(max_length=100, unique=True)
    property_type = models.CharField(
        max_length=50,
        choices=[
            ('apartment', 'Apartamento'),
            ('house', 'Casa'),
            ('land', 'Terreno'),
            ('commercial', 'Comercial'),
        ]
    )

    address = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area_sqm = models.IntegerField()
    garage_spaces = models.IntegerField(default=0)
    
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = RichTextField()
    main_image = models.ImageField(upload_to='properties/')
    
    is_available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('reference'),
            FieldPanel('property_type'),
            FieldPanel('is_available'),
            FieldPanel('featured'),
        ], heading="Informações Gerais"),
        
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('area'),
            FieldPanel('city'),
            FieldPanel('state'),
            FieldPanel('zipcode'),
        ], heading="Localização"),
        
        MultiFieldPanel([
            FieldPanel('bedrooms'),
            FieldPanel('bathrooms'),
            FieldPanel('area_sqm'),
            FieldPanel('garage_spaces')
        ], heading="Características"),
        
        FieldPanel('price'),
        FieldPanel('main_image'),
        FieldPanel('description'),
        #InlinePanel('gallery_images', label="Galeria"),
    ]
    
    parent_page_types = ['PropertyIndexPage']
    search_fields = Page.search_fields + [
        index.SearchField('address'),
        index.SearchField('description'),
    ]


class PropertyImage(models.Model):
    """Imagem da galeria"""
    property_page = models.ForeignKey(
        PropertyPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ImageField(upload_to='properties/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']