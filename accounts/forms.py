from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

attrs = {'class': 'form-control'}

class UserLoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_('UserName'),
        widget= forms.TextInput(attrs=attrs)
    )

    password = forms.CharField(
        label=_('PassWord'),
        widget= forms.PasswordInput(attrs=attrs)
    )


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First_name'),
        widget= forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label=_('Last_name'),
        widget= forms.TextInput(attrs=attrs)
    )

    username = forms.CharField(
        label=_('UserName'),
        widget= forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label=_('Email'),
        widget= forms.TextInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label=_('PassWord'),
        widget= forms.PasswordInput(attrs=attrs)
    )

    password2 = forms.CharField(
        label=_('PassWord Confirm'),
        widget= forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')



class ProfileForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }