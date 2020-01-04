"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from exam import views
# from django.views.generic.simple import redirect_to

urlpatterns = [
    #管理员登陆
    path('admin/', admin.site.urls),
    #学生登陆
    path('studentLogin/',views.studentLogin),
    # url(r'^studentLogin/',views.studentLogin),
    #教师登陆
    path('officerLogin/',views.OfficerLogin),
    
    
    #默认访问首页
    url(r'^$',views.index),
    url(r'^startExam/$',views.startExam),
    url(r'^calGrade/$',views.calGrade),
    url(r'^logout/$',views.logOut),
    url(r'^toIndex/$',views.toIndex),
    url(r'^upSingleChoice/$', views.upSingleChoice),
    url(r'^upMultiChoice/$', views.upMultiChoice),
]
