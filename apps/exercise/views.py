from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from apps.package.mixins import PackageRequiredMixin
from .models import ExerciseProgram


# Render UserExerciseProgram View
class UserExerciseProgram(LoginRequiredMixin, PackageRequiredMixin, TemplateView):
    template_name = 'exercise/exercise-program.html'
    package_type = 'workout'
    
    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        
        pk = kwargs.get('pk')
        program = get_object_or_404(ExerciseProgram, id=pk)

        contexts['exercise_program'] = program
        return contexts
