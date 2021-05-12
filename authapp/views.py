from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib import auth, messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
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
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        login_form = LoginForm()
    content = {
        'title': 'GeekShop - Авторизация',
        'login_form': login_form
    }

    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return redirect('index')


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('authapp:profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        # 'baskets': Basket.objects.all(),
    }
    return render(request, 'authapp/profile.html', context)