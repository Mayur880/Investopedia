from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home,post,category, signin, loginuser,userlogout, about,courses

urlpatterns = [
    path('', home, name="home"),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
    path('signin/', signin, name="signin"),
    path('login/', loginuser, name="loginuser"),
    path('logout/', userlogout, name="userlogout"),
    path('about/', about, name="about"),
    path('courses/', courses, name="courses"),
    ]