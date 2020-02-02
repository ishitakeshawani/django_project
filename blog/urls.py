from django.urls import path
from .import views
from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('index/',views.index,name='blog-index'),
    path('studentform/',views.student,name='blog-student'),
    path('admin/',admin.site.urls),
    ]
