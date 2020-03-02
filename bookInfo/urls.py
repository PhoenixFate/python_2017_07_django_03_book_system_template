"""python_2017_07_django_03_book_system_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index1),
    path("index/", views.index1),
    path("index2/", views.index2),
    path("temp/", views.temp_var),
    path("temp_tags/", views.template_tag),
    path("temp_filter/", views.template_filter),
    path("temp_child1/", views.template_extend),
    path("html_escape/", views.html_escape),
    path("login/", views.login),
    path("login_check/", views.login_check),
    path("change_password/", views.change_password),
    path("change_password_action/", views.change_password_action),
]
