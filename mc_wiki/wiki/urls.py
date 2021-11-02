"""mc_wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_interface, name='main'),
    re_path(r'^mc_item$', item_interface, name='item'),
    re_path(r'^mc_item/weapon/(?P<item_id>\d+)/$', item_weapon, name='weapon'),

    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
