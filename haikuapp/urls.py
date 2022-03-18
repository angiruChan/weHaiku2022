from django.urls import path
from . import views

app_name = 'haikuapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_home/<str:id>/", views.user_home, name="user_home"),
]
