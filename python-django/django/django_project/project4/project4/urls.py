"""project4 URL Configuration

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
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("test/", views.test, name="test"),
    path("test_01/", views.test_01, name="test_01"),
    path('test_02/if/', views.test_02_if, name="test_02_if"),
    path('test_02/for/', views.test_02_for, name="test_02_for"),
    path('test_02/endfor/', views.test_02_endfor, name="test_02_endfor"),
    # การใช้แท็ก url
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),

    # กรณีที่พาธนั้นมีพารามิเตอร์
    path('tag/auto-escape/', views.tag_auto_escape),

    # การใช้ filter
    path('filter/str-list-num/', views.filter_str_list_num),

    # การใช้ filter เกี่ยวกับ ตัวเลข
    path('filter/num/', views.filter_num),

    # การใช้ filter เกี่ยวกับ สตริง
    path('filter/string/', views.filter_string)
]
