from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
                return redirect('/user_home')
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


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect("/user_login")


def index(request):
    link_active_home = True
    visitor_access = True
    return render(request, 'haikuapp/index.html', {
        "visitor_access": visitor_access,
        "link_active_home": link_active_home,
    })


@login_required(login_url='/user_login/')
def user_home(request):
    if request.user.is_authenticated:
        return render(request, 'haikuapp/user_home.html', {
            "user_logged_in": True,
        })
    else:
        HttpResponse("access not granted")


def submit_an_entry(request):
    link_active_entry = True
    visitor_access = True
    success = False
    line1 = ''
    line2 = ''
    line3 = ''
    form = EntryForm(request.POST)

    if request.method == "POST":
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        line3 = request.POST['line3']
        myHaiku = haiku_entry_combine(line1, line2, line3)
        if form.is_valid():
            # create entry
            myEntry = form.save(commit=False)
            myEntry.haiku_entry = myHaiku
            myEntry.entry_status = get_object_or_404(Entry_Status, entry_status="pending")
            myEntry.save()
            form = EntryForm
            success = True
            line1 = ''
            line2 = ''
            line3 = ''
        else:
            form.errors
    else:
        form = EntryForm

    return render(request, 'haikuapp/submit_an_entry.html', {
        "visitor_access": visitor_access,
        "link_active_entry": link_active_entry,
        "form": form,
        "success": success,
        "line1": line1,
        "line2": line2,
        "line3": line3,
    })


@login_required(login_url='/')
def user_haiku_entries(request):
    if request.user.is_authenticated:
        user_logged_in = True
        haiku = Entry.objects.all().order_by('-date_created')
        err_msg = ''
        ss_msg = ''
        form = EntryForm(request.POST)

        if request.method == "POST":
            line1 = request.POST['line1']
            line2 = request.POST['line2']
            line3 = request.POST['line3']
            myHaiku = haiku_entry_combine(line1, line2, line3)
            if form.is_valid():
                # create entry
                myEntry = form.save(commit=False)
                myEntry.haiku_entry = myHaiku
                myEntry.entry_status = get_object_or_404(Entry_Status, entry_status="pending")
                myEntry.save()
                form = EntryForm
                ss_msg = "Successfully Added!"
            else:
                form.errors
                err_msg = "There are errors in some fields."
        else:
            form = EntryForm

        return render(request, 'haikuapp/user_haiku_entries.html', {
            "haiku": haiku,
            "user_logged_in": user_logged_in,
            "form": form,
            "ss_msg": ss_msg,
            "err_msg": err_msg,
        })
    else:
        HttpResponse("access not granted")


def haiku_entry_combine(line1, line2, line3):
    myHaiku = line1 + " / " + line2 + " / " + line3
    return myHaiku
