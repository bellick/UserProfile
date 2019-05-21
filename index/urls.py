from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('',views.main),
    re_path(r"^index/(\w+)/$",views.index,name='main-view'),
]