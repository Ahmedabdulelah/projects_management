from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm
from accounts.views import Registration, edit_profile

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', Registration.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]