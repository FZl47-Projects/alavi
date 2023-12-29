from django.shortcuts import redirect


# LogoutRequired Mixin
class LogoutRequiredMixin:
    """ Allow access only to unauthorized users """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect('public:index')


# ProfileVerified Mixin
class ProfileVerifiedMixin:
    """ Allow access only to verified users """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login_register')

        # Check UserProfile verification
        if not request.user.user_profile.verified:
            user = request.user
            # Create unique token for UserProfile (to track user authentication)
            user.user_profile.generate_token()

            # Save token in sessions (temporary) and redirect user to GetProfileInfo view
            request.session['register_token'] = user.user_profile.token
            return redirect('account:register_profile')

        return super().dispatch(request, *args, **kwargs)
