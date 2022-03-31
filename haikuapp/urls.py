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
    path("add_haiku_entries/", views.add_haiku_entries, name="add_haiku_entries"),
    path("update_haiku_entries/<str:h_id>/", views.update_haiku_entries, name="update_haiku_entries"),
    path("delete_haiku_entry/", views.delete_haiku_entry, name="delete_haiku_entry"),
    path("user_categories/", views.user_categories, name="user_categories"),
]
