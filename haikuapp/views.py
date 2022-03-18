from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .encryption_util import encrypt, decrypt
from .forms import *


def user_login(request):
    login_page = True
    message = ''
    if request.method == "POST":
        form = AuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/user_home/' + str(encrypt(user.id)))
            else:
                message = "Invalid username or password."
        else:
            message = "Invalid username or password."

    form = AuthForm()
    return render(request, "haikuapp/user_login.html", {
        "login_form": form,
        'message': message,
        'login_page': login_page,
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect("/user_login")


def index(request):
    visitor_access = True
    return render(request, 'haikuapp/index.html', {"visitor_access": visitor_access})


def user_home(request, id):
    decrypt_id = decrypt(id)
    user_logged_in = True
    return render(request, 'haikuapp/user_home.html', {
        "user_logged_in": user_logged_in,
        "decrypt_id": decrypt_id,
    })
