from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import LoginForm, RegisterForm, UserProfileForm
from basketapp.models import Basket

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView, CreateView


class RegisterView(CreateView):
    template_name = 'authapp/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('authapp:login')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'authapp/login.html'

    def get_success_url(self):
        return reverse_lazy('mainapp:products')


@method_decorator(login_required, name='dispatch')
class Logout(LogoutView):
    success_url = reverse_lazy('mainapp:index')


@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    form_class = UserProfileForm
    model = get_user_model()
    template_name = 'authapp/profile.html'
    success_url = reverse_lazy('mainapp:products')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context.update({'title': 'GeekShop - Личный кабинет', 'baskets': Basket.objects.filter(user=self.kwargs['pk'])})
        return context
