from django import forms
from .models import *
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


# submit an entry form
class EntryForm(forms.ModelForm):
    THEMES = {
        ('', '---------'),
        ('human nature', 'human nature'),
        ('nature and seasons', 'nature and seasons'),
        ('others', 'others'),
    }

    # custom fields
    full_name = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 254}))
    haiku_title = forms.CharField(label="", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    author_alias = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'maxlength': 250}))
    haiku_theme = forms.ChoiceField(choices=sorted(THEMES), label="", initial='',
                                    widget=forms.Select(attrs={'class': 'form-select'}), required=True)
    entry_status = forms.ModelChoiceField(queryset=Entry_Status.objects.all(), label="",
                                          widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Entry
        fields = ("full_name", "email", "haiku_title", "author_alias", "haiku_theme", "entry_status")


class EntryStatusForm(forms.ModelForm):
    class Meta:
        model = Entry_Status
        fields = ("entry_status",)
