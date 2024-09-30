from django.shortcuts import render, redirect
from .models import Car_details
from .forms import CarForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.

def home(request):
    cars = Car_details.objects.all()
    return render(request, 'home.html', {'cars': cars})

@login_required
def viewDetails(request, car_id):
    car = Car_details.objects.get(id=car_id)
    return render(request, 'viewDetails.html', {'car': car})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after saving
    else:
        form = CarForm()
    
    return render(request, 'add_car.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login_view.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect(home)
   