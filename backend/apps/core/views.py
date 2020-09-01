from django.views.generic import TemplateView

class IndexView(TemplateView):
    
    def get_template_names(self):
        template_name = 'index.html'
        return template_name