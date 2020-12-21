from django.conf import settings
from django.views.generic import TemplateView

class IndexView(TemplateView):
    
    def get_template_names(self):

        if settings.DEBUG:
            template_name = 'index-dev.html'
        else:
            template_name = 'index.html'

        return template_name