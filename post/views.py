from django.shortcuts import render

# Create your views here.

def show_post(request):
    return render(
        request,
        'post/index.html',
    )
    
def login(request):
    return render(
        request,
        'post/login.html',
    )

    
def register(request):
    return render(
        request,
        'post/register.html',
    )