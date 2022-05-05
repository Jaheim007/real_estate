from django.shortcuts import render, redirect
from . import forms
from .forms import SignupForm

def index(request): 
    return render(request, 'estateHTML\index.html')

def login_page(request):
    form = forms.Log()
    if request.method == 'POST':
        form = forms.Log(request.POST)
        if form.is_valid():
            return redirect('home')
    return render(request, 'estateHTML\log.html', context={'form': form})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    return render(request, 'estateHTML\sign.html', context={'form': form})

def home(request):
    return render(request, 'estateHTML\main.html' ,)
    

# Create your views here.
