from allauth.account import forms
from allauth.account.forms import SignupForm
from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser

class CustomSingUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Adres Email')