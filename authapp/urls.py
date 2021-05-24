from django.urls import path
from .views import Login, RegisterView, Logout, ProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
