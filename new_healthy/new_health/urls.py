"""new_health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from health import views
from django.conf.urls import url
from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('index/', views.index),
    path('emg/', views.emg),
    path('spo2/', views.spo2),
    path('electrocardiogram/', views.electrocardiogram),
    path('login/', views.login),
    path('sign_out/', views.sign_out),
    path('register/', views.register),
    path('test/', views.test),
    path('clean/', views.clean),
    # path('ele/', views.ele),
]
