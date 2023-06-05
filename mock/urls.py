"""
URL configuration for mock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    path('register/',register,name='register'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('insert_question/',insert_question,name='insert_question'),
    path('list_ques/',list_ques.as_view(),name='list_ques'),
    path('insert_answer/',insert_answer,name='insert_answer'),


    re_path('(?P<pk>\d+)/',details.as_view(),name='details'),
]
