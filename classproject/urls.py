"""classproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('registerform/',registerform,name='registerform'),
    path('userelog/',userlog,name='userlog'),
    path('userout/',userout,name='userout'),
    path('questions/',questions,name='questions'),
    path('answers/',answers,name='answers'),
    path('Questionlist/',Questionlist.as_view(),name='Questionlist'),

    re_path('(?P<pk>\d+)/',Questiondetail.as_view(),name='Questiondetail'),
]
