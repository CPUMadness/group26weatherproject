import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

API_KEY = 'REPLACE_THIS_WITH_YOUR_OWN_KEY'

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    weather = None
    if 'city' in request.GET:
        city = request.GET['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temp': data['main']['temp'],
                'desc': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
    return render(request, 'dashboard.html', {'weather': weather})
