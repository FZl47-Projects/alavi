from functools import wraps
from django.shortcuts import redirect
from django.conf import settings


def admin_required(roles=settings.ADMIN_USER_ROLES):
    def wrapper(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            user = request.user
            if user is None or user.is_anonymous:
                return redirect('account:login_register')
            role = user.role
            if not (role in roles):
                return redirect('account:login_register')
            return func(request, *args, **kwargs)

        return inner

    return wrapper


def admin_required_cbv(roles=settings.ADMIN_USER_ROLES):
    def wrapper(func):
        @wraps(func)
        def inner(self, request, *args, **kwargs):
            user = request.user
            if user is None or user.is_anonymous:
                return redirect('account:login_register')
            role = user.role
            if not (role in roles):
                return redirect('account:login_register')
            return func(self, request, *args, **kwargs)

        return inner

    return wrapper
