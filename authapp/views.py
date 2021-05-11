from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import auth


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('authapp:login')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context)


def login(request):
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect('index')

    content = {
        'title': 'GeekShop - Авторизация',
        'login_form': login_form
    }

    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return redirect('index')
