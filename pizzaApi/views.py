from django.shortcuts import redirect

def empty_url(request):
    return redirect('docs/')