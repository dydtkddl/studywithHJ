from django.urls import path
from . import views 
urlpatterns = [

    path("home/", views.home),
    path("/", views.home),
    path("write/", views.write),
    path("save_article_json/", views.save_article_json),
    path("read_article_json/", views.read_article_json),
    path("read_article/", views.read_article),
    path("signup/", views.signup),
    path("login/", views.login),
    path("logout/", views.logout),
    path("comment/save/", views.Comment_request.save),
    path("comment/show/", views.Comment_request.show),
]