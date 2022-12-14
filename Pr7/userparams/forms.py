from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


# registration form
class Registrationform(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {"email": "Email"}


# user login for here we give some bootstrap classes in our form

class user_login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control form-control-lg"}))
