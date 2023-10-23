from django.views.generic import TemplateView
from .models import Certificate, FreeDietProgram


# Render Index View
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts['certificates'] = Certificate.objects.all()

        return contexts


# Render FreeDietProgram
class FreeDietProgramView(TemplateView):
    template_name = 'public/diet-free.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts['diet_program'] = FreeDietProgram.objects.last()

        return contexts
