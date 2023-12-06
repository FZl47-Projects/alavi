from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from apps.package.mixins import PackageRequiredMixin
from .models import DietProgram


class UserDietProgram(LoginRequiredMixin, PackageRequiredMixin, TemplateView):
    template_name = 'program/diet-program.html'
    package_type = 'diet'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        pk = kwargs.get('pk')
        program = get_object_or_404(DietProgram, pk=pk)

        contexts['diet_program'] = program
        return contexts
