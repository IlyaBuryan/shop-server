from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from .forms import UserAdminRegisterForm, UserAdminProfileForm, AdminProductCategoryForm, AdminProductForm
from mainapp.models import ProductCategory, Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class LoginMixin:
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


# # CRUD - Create Read Update Delete
class AdminUsersRead(LoginMixin, ListView):
    model = get_user_model()
    template_name = 'adminapp/admin-users-read.html'


class AdminUserCreateView(LoginMixin, CreateView):
    model = get_user_model()
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admin_staff:admin_users_read')


class AdminUserUpdateView(LoginMixin, UpdateView):
    model = get_user_model()
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        context = super(AdminUserUpdateView, self).get_context_data()
        context.update({'selected_user': get_user_model().objects.get(pk=self.kwargs['pk'])})
        return context


class AdminUserDeleteView(LoginMixin, DeleteView):
    model = get_user_model()
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class AdminCategoriesRead(LoginMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-read.html'


class AdminCategoryCreateView(LoginMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-create.html'
    form_class = AdminProductCategoryForm
    success_url = reverse_lazy('admin_staff:admin_categories_read')


class AdminCategoriesUpdateView(LoginMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_categories_read')
    form_class = AdminProductCategoryForm

    def get_context_data(self, **kwargs):
        context = super(AdminCategoriesUpdateView, self).get_context_data()
        context.update({'selected_category': ProductCategory.objects.get(pk=self.kwargs['pk'])})
        return context


class AdminCategoryDeleteView(LoginMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_categories_read')


class AdminProductsRead(LoginMixin, ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'


class AdminProductCreateView(LoginMixin, CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = AdminProductForm
    success_url = reverse_lazy('admin_staff:admin_products_read')


class AdminProductUpdateView(LoginMixin, UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_products_read')
    form_class = AdminProductForm

    def get_context_data(self, **kwargs):
        context = super(AdminProductUpdateView, self).get_context_data()
        context.update({'selected_product': Product.objects.get(pk=self.kwargs['pk'])})
        return context


class AdminProductDeleteView(LoginMixin, DeleteView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_products_read')
