from django.views.generic import TemplateView
import os

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = os.environ.get('TITLE','')
        return context
    