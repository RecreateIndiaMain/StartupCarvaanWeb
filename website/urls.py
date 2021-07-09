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
    path('join/', join, name="joinus_page"),
    path('startups/', startups, name = 'startup_page'),
    path('users/', users, name = 'users_page'),
    path('table/', table, name = 'table_page'),
    path('dashboard/', dashboard, name = 'dash_page'),
    path('help-dash/', helpdash, name = 'help_dash_page'),
    path('blog/', blog, name = 'blog_page'),
    path('startup-blog/', startabout, name = 'startup_blog'),
    path('profile/', userprofile, name = 'profile_page'),
    path('addblog/', addblog, name = 'add_blog'),
    path('help/', help, name = 'help_page'),
    path('',home, name = 'home_page'),
    path('registerUser/',registerUser),
    path('competition/', competition, name = 'competition'),
    path('forgot/', forgot, name = "forgot_password"),
    path('join-dash/', joindash, name = 'joindash'),
    path('comp-dash/', compdash, name = 'compdash'),
    path('help-dash/delete_help/<str:id>', delete_help, name = 'delete_help'),
    path('help-dash/accept_help/<str:id>', accept_help, name = 'accept_help'),
    path('join-dash/accept_join/<str:id>', accept_join, name = 'accept_join'),
    path('join-dash/delete_join/<str:id>', delete_join, name = 'delete_join'),
    path('comp-dash/accept_comp/<str:id>', accept_comp, name = 'accept_comp'),
    path('comp-dash/delete_comp/<str:id>', delete_comp, name = 'delete_comp'),
    path('logout/', logout, name = 'logout'),
    path('payment/',payment,name='payment'),
    path('status/<slug:id>',status,name='status'),
    path('successful',successful,name='successful'),
    path('checkpayment',checkPayment,name='checkpayment')
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)