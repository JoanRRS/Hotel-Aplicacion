from django.shortcuts import redirect
from functools import wraps

def unauthenticated_user(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home page if user is authenticated
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
