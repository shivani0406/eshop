from django.shortcuts import redirect




from django.shortcuts import redirect

def auth_middleware(get_response):
    def middleware(request):
        # Check if the user is not authenticated and the current URL is not the login page
        if not request.session.get('customer') and request.path != '/login/':
            return redirect('login')  # Redirect to the login page
        else:
            response = get_response(request)
            return response

    return middleware
