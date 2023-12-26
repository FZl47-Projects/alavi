from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from apps.order.models import PurchaseRequest
from apps.package.models import Package


# PackageRequest view
class PackageRequestView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        package = get_object_or_404(Package, id=self.request.GET.get('pk'))
        user = self.request.user

        try:
            purchase_request = PurchaseRequest.objects.get(user=user)
        except PurchaseRequest.DoesNotExist:
            purchase_request = PurchaseRequest.objects.create(user=user)

        if not purchase_request.package.filter(id=package.id).exists():
            purchase_request.package.add(package)

        return package.buy_link
