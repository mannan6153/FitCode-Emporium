from django.shortcuts import render, get_object_or_404
from .models import Login

# Create your views here.

def landingpage(request):
    return render(request, 'landingpage.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def blog(request):
    return render(request, 'blog.html')

def blogpage(request):
    return render(request, 'blogpage.html')

def cart(request):
    return render(request, 'cart.html')

def feedback(request):
    return render(request, 'feedback.html')

def login(request):
    try:
        login = Login.objects.all()
    except Login.DoesNotExist:
        login = None
    return render(request, 'login.html', {'login': login})

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

def shop(request):
    return render(request, 'shop.html')

def contactus(request):
    return render(request, 'contactus.html')
