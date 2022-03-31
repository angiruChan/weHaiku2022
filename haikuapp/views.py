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
    default_status = get_object_or_404(Entry_Status, entry_status="pending")

    if request.method == "POST":
        form = EntryForm(request.POST)
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        line3 = request.POST['line3']
        myHaiku = haiku_entry_combine(line1, line2, line3)
        if form.is_valid():
            # create entry
            myEntry = form.save(commit=False)
            myEntry.haiku_entry = myHaiku
            myEntry.entry_status = default_status
            myEntry.save()
            form = EntryForm()
            success = True
            line1 = ''
            line2 = ''
            line3 = ''
        else:
            form.errors
    else:
        form = EntryForm()

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
        return render(request, 'haikuapp/user_haiku_entries.html', {
            "haiku": haiku,
            "user_logged_in": user_logged_in,
        })
    else:
        HttpResponse("access not granted")


@login_required(login_url='/')
def add_haiku_entries(request):
    if request.user.is_authenticated:
        title = 'Add Haiku Entry'
        user_logged_in = True
        line1 = ''
        line2 = ''
        line3 = ''
        success_msg = ''

        if request.method == "POST":
            form = EntryForm(request.POST)
            line1 = request.POST['line1']
            line2 = request.POST['line2']
            line3 = request.POST['line3']
            myHaiku = haiku_entry_combine(line1, line2, line3)

            if form.is_valid():
                # create entry
                myEntry = form.save(commit=False)
                myEntry.haiku_entry = myHaiku
                myEntry.save()
                form = EntryForm()
                success_msg = "Successfully Added!"
                line1 = ''
                line2 = ''
                line3 = ''
            else:
                form.errors
        else:
            form = EntryForm()

        return render(request, 'haikuapp/haiku_entry.html', {
            "user_logged_in": user_logged_in,
            "form": form,
            "line1": line1,
            "line2": line2,
            "line3": line3,
            "title": title,
            "success_msg": success_msg,
        })
    else:
        HttpResponse("access not granted")


@login_required(login_url='/')
def update_haiku_entries(request, h_id):
    title = 'Update Haiku Entry'
    entry = get_object_or_404(Entry, pk=decrypt(h_id))
    user_logged_in = True
    line1 = entry.haiku_entry.split("/")[0]
    line2 = entry.haiku_entry.split("/")[1]
    line3 = entry.haiku_entry.split("/")[2]
    success_msg = ''

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        line3 = request.POST['line3']
        if form.is_valid():
            myEntry = form.save(commit=False)
            myEntry.haiku_entry = haiku_entry_combine(line1, line2, line3)
            myEntry.save()
            success_msg = "Successfully Updated"
        else:
            return HttpResponse(form.errors.values())
    else:
        form = EntryForm(instance=entry)

    return render(request, 'haikuapp/haiku_entry.html',{
        "user_logged_in": user_logged_in,
        "form": form,
        "line1": line1,
        "line2": line2,
        "line3": line3,
        "title": title,
        "success_msg": success_msg,
    })


@login_required(login_url='/')
def delete_haiku_entry(request):
    if request.method == "POST":
        confirm_delete = request.POST['confirm_delete']
        print(confirm_delete)
        e_haiku = get_object_or_404(Entry, pk=decrypt(confirm_delete))
        e_haiku.delete()
        return redirect('/user_haiku_entries')
    else:
        pass


def haiku_entry_combine(line1, line2, line3):
    myHaiku = line1 + " / " + line2 + " / " + line3
    return myHaiku


@login_required(login_url='/')
def user_categories(request):
    if request.user.is_authenticated:
        user_logged_in = True
        categories = Category.objects.all().order_by('-date_created')
        return render(request, 'haikuapp/user_categories.html', {
            "categories": categories,
            "user_logged_in": user_logged_in,
        })
    else:
        HttpResponse("access not granted")


