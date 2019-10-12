from allauth.account.forms import LoginForm, SignupForm
from allauth.socialaccount.models import SocialAccount
from allauth.compat import ugettext, ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class CustomLoginForm(LoginForm):

    error_messages = {
        'account_inactive':
        _("Esta cuenta es inactiva."),

        'email_password_mismatch':
        _("El correo/ó la contraseña especificados no son correctos."),
    }

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.pop("autofocus", None)

class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password':forms.PasswordInput()
        }


