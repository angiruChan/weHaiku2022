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
    path("user_haiku/", views.user_haiku, name="user_haiku"),
    path("add_category/", views.add_category, name="add_category"),
    path("update_category/<str:c_id>/", views.update_category, name="update_category"),
    path("delete_category/", views.delete_category, name="delete_category"),
    path("add_haiku/", views.add_haiku, name="add_haiku"),
    path("update_haiku/<str:h_id>/", views.update_haiku, name="update_haiku"),
    path("delete_haiku/", views.delete_haiku, name="delete_haiku"),
    path("comments/<str:c_id>", views.comments, name="comments"),
    path("user_comments/", views.user_comments, name="user_comments"),
    path("update_comment/<str:c_id>", views.update_comment, name="update_comment"),
    path("about_us_page/", views.about_us_page, name="about_us_page"),
]
