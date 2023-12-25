from django.views.generic import TemplateView
from .models import Certificate, FreeContent
from apps.package.models import Package


# Render Index View
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        contexts['packages'] = Package.objects.all()[:4]
        contexts['certificates'] = Certificate.objects.all()

        return contexts
