"""
URL configuration for genshinforum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.index, name='main'),
    path('tabl/', views.tabl, name='tabl'),
    path('themes/', views.themes, name='themes'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('themes/<int:theme_id>', views.themesinside, name='insidetheme'),
    path('my_profile/', lk, name='lk'),  # Use views.lk here
]
