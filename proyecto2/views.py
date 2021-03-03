from django.views.generic.base import TemplateView

class HomePage (TemplateView):
    template_name = 'Home.html'
class ContenidoPage (TemplateView):
    template_name = 'Contenido.html'
class AcercaDe (TemplateView):
    template_name = 'AcercaDe.html'

