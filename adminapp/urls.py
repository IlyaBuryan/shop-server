from django.urls import path
from .views import index, AdminUsersRead, AdminUserCreateView, AdminUserUpdateView, AdminUserDeleteView, \
    AdminProductsRead, AdminCategoriesRead, AdminCategoryCreateView, AdminCategoriesUpdateView, \
    AdminCategoryDeleteView, AdminProductCreateView, AdminProductUpdateView, AdminProductDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', AdminUsersRead.as_view(), name='admin_users_read'),
    path('admin-users-create/', AdminUserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', AdminUserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-remove/<int:pk>/', AdminUserDeleteView.as_view(), name='admin_users_remove'),

    path('admin-categories-read/', AdminCategoriesRead.as_view(), name='admin_categories_read'),
    path('admin-categories-create/', AdminCategoryCreateView.as_view(), name='admin_categories_create'),
    path('admin-categories-update/<int:pk>/', AdminCategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('admin-categories-remove/<int:pk>/', AdminCategoryDeleteView.as_view(), name='admin_categories_remove'),

    path('admin-products-read/', AdminProductsRead.as_view(), name='admin_products_read'),
    path('admin-products-create/', AdminProductCreateView.as_view(), name='admin_products_create'),
    path('admin-products-update/<int:pk>/', AdminProductUpdateView.as_view(), name='admin_products_update'),
    path('admin-products-remove/<int:pk>/', AdminProductDeleteView.as_view(), name='admin_products_remove'),
]
