from django.views.generic import ListView
from .models import Package


# ProductsList view
class ProductListView(ListView):
    template_name = 'package/packages_list.html'
    model = Package
    context_object_name = 'packages'
