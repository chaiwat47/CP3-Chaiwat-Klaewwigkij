from django.http import HttpResponse
from django.shortcuts import render

# การเขียน url แบบ statics
def index(request):
    # แสดงผลไฟล์ index.html ที่สร้างไว้ในโฟลเดอร์ templates (ไม่ต้องระบุชื่อโฟลเดอร์)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# เรียกใช้ไฟล์.html จากโฟลเดอรฺที่สร้างไว้
def product_detail(request):
    return render(request, 'products/detail.html')

def signin(request):
    return render(request, 'members/signin.html')

def test(request):
    vars = {'title': 'Django Framework', 'message':'Hi world'}
    return render(request, 'test.html', vars)

# ทดสอบการแทรกค่าตัวแปรชนิดข้อมูลต่างๆ
# 1.แบบ {{}}
from datetime import date

def test_01(request):
    dt = date.today()
    data = {
        'colors': ['red', 'green', 'blue'],
        'flowers': {'a': 'rose', 'b': 'jasmine', 'c': 'orchid'},
        'date': dt # object
    }
    return render(request, 'test_01.html', data)

# 2.แบบ {% %}
# tag_if

def test_02_if(request):
    vars = { 'home_goals':2, 'guest_goals':2}
    return render(request, 'test_02_if.html', vars)

# tag_for
# {%for%}
# {%empty%}
# {%cycle%}

def test_02_for(request):
    vars = {
        'range': range(1, 6),
        'list': ['red', 'green', 'blue', 'yellow'],
        'dict': {'a':'ant', 'b':'boy', 'c':'cat', 'd':'dog'}
    }
    return render(request, 'test_02_for.html', vars)

def test_02_endfor(request):
    vars = {
        'range': range(1, 6),
        'list': ['red', 'green', 'blue', 'yellow'],
        'dict': {'a':'ant', 'b':'boy', 'c':'cat', 'd':'dog'}
    }
    return render(request, 'test_02_endfor.html', vars)

def contact(request):
    return render(request, 'test_02_url_tag.html')

def home(request):
    return render(request, 'test_02_url_tag.html')

def tag_auto_escape(request):
    data = { 'html_str': '<b>\"Tom\" & "Jerry"</b>'}
    return render(request, 'tag-auto-escape.html', data)

def filter_str_list_num(request):
    data = {
            'var_str': 'Hello world',
            'var_list': ['One', 'Two', 'Three'],
            'var_int': 2475,
            'var_float': 3.14,
            'var_none': None,
            }
    return render(request, 'filter-str-list-num.html', data)

def filter_num(request):
    data = {
            'hahaha':555,
            'filesize':387504257,
            'num_int':1234,
            'num_float':1234.56789
    }
    return render(request, 'filter-num.html', data)

def filter_string(request):
    data = {
        'str1': 'Model Template View',
        'str2': 'model <br>\nview<br>\nconroller',
        'str3': 'django is the web framework',
        'str4': "<b>Don't repeat yourself (DRY)</b>",
        'str5': '<b><a href=#>Click Here</a> to download</b>'
    }
    return render(request, 'filter-string.html', data)