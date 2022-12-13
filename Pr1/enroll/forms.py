from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# here we want to add some more fields in our registraion form so we inherit our usermodel for taking all the feilds in our registraion form
# we inherit here UserCreationForm so we don't need to give thes username and password fields becasue these field will be inherit in our form


class Custom_signupform(UserCreationForm):
    password2 = forms.CharField(
        label="Password Re-Enter", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {"email": "Email"}
