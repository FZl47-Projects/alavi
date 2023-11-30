from django.shortcuts import redirect


# LogoutRequired Mixin
class LogoutRequiredMixin:
    """ Allow access only to unauthorized users """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('public:index')
