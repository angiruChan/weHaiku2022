from django.urls import path
from . import views

app_name = 'haikuapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_home/", views.user_home, name="user_home"),
    path("submit_an_entry/", views.submit_an_entry, name="submit_an_entry"),
    path("user_haiku_entries/", views.user_haiku_entries, name="user_haiku_entries"),
    path("haiku_entries/<str:value>", views.haiku_entries, name="haiku_entries"),
]
