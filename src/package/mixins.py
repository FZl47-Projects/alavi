from django.http import Http404


# PackageRequired Mixin
class PackageRequiredMixin:
    """ Allow access only to users that has packages """
    package_type = ''

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        package_name = self.package_type

        if user.is_admin_user or user.has_package(package_name):
            return super().dispatch(request, *args, **kwargs)

        raise Http404
