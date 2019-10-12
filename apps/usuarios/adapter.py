from django.contrib.auth.models import User
from allauth.account.adapter import DefaultAccountAdapter
from allauth.compat import ugettext, ugettext_lazy as _

class CustomAdapter(DefaultAccountAdapter):
    error_messages = {
        'username_blacklisted':
        _('Username can not be used. Please use other username.'),
        'username_taken':
        User._meta.get_field('username').error_messages['unique'],
        'too_many_login_attempts':
        _('Demasiados intentos de inicio de sesion. Intente mas tarde.'),
        'email_taken':
        _("Este correo ya ha sido registrado."),
    }