from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def user_logged_in(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id = request.session.get('user_id') 
        if user_id:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'You need to be logged in to place an order.')
            return redirect('login') 

    return _wrapped_view