from re import L
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    '''
    if request.user.is_authenticated:
        return render(request, "accounts/already-logged-in.html", {})
    '''

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)    
            return redirect('/')
        else:
            form = AuthenticationForm(request)   
    return render(request, "accounts/login.html", {})

def logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('/logout')
    return render(request, "acounts/logout.html", {})

def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "acounts/register.html", {})    