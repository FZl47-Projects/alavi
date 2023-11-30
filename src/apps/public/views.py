from django.views.generic import TemplateView
from .models import Certificate, FreeExerciseProgram
from apps.package.models import Package


# Render Index View
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        contexts['packages'] = Package.objects.all()[:4]
        contexts['certificates'] = Certificate.objects.all()

        return contexts


# Render FreeExerciseProgram
class FreeExerciseProgramView(TemplateView):
    template_name = 'public/exercise_free.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        try:
            program = FreeExerciseProgram.objects.get(is_active=True)
        except (FreeExerciseProgram.DoesNotExist, FreeExerciseProgram.MultipleObjectsReturned):
            program = FreeExerciseProgram.objects.last()

        contexts['exercise_program'] = program

        return contexts
