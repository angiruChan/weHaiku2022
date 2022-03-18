from django import forms
from django.contrib.auth.forms import AuthenticationForm


# login form
class AuthForm(AuthenticationForm):

    # accept all the argument
    def __init__(self, *args, **kwargs):
        # Calling the parent class's initializer
        super(AuthForm, self).__init__(*args, **kwargs)

    # custom fields
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}))
