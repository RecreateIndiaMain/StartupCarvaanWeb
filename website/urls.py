"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('startuplogin/', startuplogin, name="login_page"),
    path('userlogin/', userlogin, name="login_page"),
    path('join/', join, name="joinus_page"),
    path('startups/', startups, name = 'startup_page'),
    path('users/', users, name = 'users_page'),
    path('table/', table, name = 'table_page'),
    path('dashboard/', dashboard, name = 'dash_page'),
    path('help-dash/', helpdash, name = 'help_dash_page'),
    path('blog/', blog, name = 'blog_page'),
    path('startup-blog/', startabout, name = 'startup_blog'),
    path('profile/', userprofile, name = 'profile_page'),
    path('addblog/', addBlogPage, name = 'add_blog'),
    path('help/', help, name = 'help_page'),
    path('',home, name = 'home_page'),
    path('registerUser/',registerUser),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)