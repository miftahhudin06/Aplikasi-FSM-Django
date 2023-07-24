from functools import wraps

from django.shortcuts import redirect


def hanya_admin(user):
    if user.is_admin:
        return True
    return False


def hanya_teknisi(user):
    if user.is_teknisi:
        return True
    return False


def akses_admin():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not hanya_admin(request.user):
                return redirect('home')
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator
