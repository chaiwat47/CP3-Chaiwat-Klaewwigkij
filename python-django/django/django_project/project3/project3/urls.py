"""project3 URL Configuration

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
from django.urls import path
from django.urls import path, re_path # สำหรับการกำหนด path แบบ RegEx
from . import views

urlpatterns = [
    # การเขียน path url แบบ statics
    path('', views.index),
    path('about/', views.about),
    path('book/programming/python/', views.book_python),
    path('course/online/python/django/chap/01/', views.dj_ch01),
    path('course/online/python/django/chap/02/', views.dj_ch02),

    # การเขียน path url แบบ parameter
    path('search/<str:keyword>/<int:page>/', views.search),
    path('date/<int:year>-<int:month>-<int:day>/', views.date),
    path('redirect/<path:url>', views.redirect),
    path('article/<int:id>/<slug:title>/', views.show_article),

    # การเขียน path url แบบ RegEx
    # ต้องเขียน repath แทน path
    # re_path(route, view)
    re_path('^drink/(?P<dnk>(coffee)|(tea)|(wine))/$', views.drink),
    re_path(r'^title/(?P<title>[-\w\s]+)/$', views.show_title),
    re_path(r'^find/(?P<key>[\w\s]+)/(?P<page>\d+)/$', views.find),
    # การอ่านค่าจาก path ที่ไม่กำหนดชื่อ pattern
    # จากเดิมคือ re_path('^drink/(?P<dnk>(coffee)|(tea)|(wine))/$', views.drink) ไม่ต้องกำหนดชื่อแล้ว
    # re_path('^drink/((coffee)|(tea)|(wine))/$', views.drink)

    # การตั้งชื่อให้กับ path
    # path(route, view, name='ref_name')
    # re_path(routh, view, name='ref_name')
    # static path:
    # path(route, view, naeme='ref_name')
    # RegEx
    # re_path(route, view, name='ref_name')
   
    # การกำหนดขเอมูลแบบ Query String
    path('maps/', views.maps),
    
    # Test- urls=parameters
    # 1.http://127.0.0.1:8000/search/django%20framework/5/
    # 2.http://127.0.0.1:8000/date/2020-02-24/
    # 3.http://127.0.0.1:8000/redirect/http://www.develoerthai.com/books/
    # 4.http://127.0.0.1:8000/article/1234/what-is-django/

    # Test- urls=RegEx
    # 1.http://127.0.0.1:8000/drink/tea/ or http://127.0.0.1:8000/drink/coffee/ or http://127.0.0.1:8000/drink/wine/
    # 2.http://127.0.0.1:8000/find/python%20django/1/ or http://127.0.0.1:8000/find/python%20django/2/

]
