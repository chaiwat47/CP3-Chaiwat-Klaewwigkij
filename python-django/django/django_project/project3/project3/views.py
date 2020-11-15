from django.http import HttpResponse

# การเขียน url แบบ statics
def index(request):
    return HttpResponse('Welcome')

def about(request):
    return HttpResponse('This is a test of Django framework')

def book_python(request):
    return HttpResponse('การเขียนโปรแกรมด้วย Python สำหรับผู้เริ่มต้น')

def dj_ch01(request):
    return HttpResponse('Django Chapter 1: Initial Setup')

def dj_ch02(request):
    return HttpResponse('Django Chapter 2: Create a Django app')



# การเขียน url แบบ parameter

def search(request, keyword, page):
    return HttpResponse(f'Search for : {keyword} page: {page}')

def date(request, day, month, year):
    return HttpResponse(f'Date: {day}-{month}-{year}')

def redirect(request, url):
    return HttpResponse(f'<a href="{url}" target="_blank"> \
                        Click here to redirect</a>')
def show_article(request, id, title):
    return HttpResponse(f'ID: {id} <br>Title: {title}')    

# การเขียน path url แบบ RegEx

def drink(request, dnk):
    return HttpResponse(f'Drink: {dnk}')

def show_title(request, title):
    return HttpResponse(f'Title: {title}')

def find(request, key, page):
    page = int(page) # แปลงสตริงเป็นจำนวนเต็ม
    prev = ''
    if page>1:
        prev = f'<a href="/find/{key}/{page-1}">Previous</a>'
    else:
        prev = ''
    
    next = f'<a href="/find/{key}/{page+1}">Next</a>'

    return HttpResponse(f'{prev}&nbsp;&nbsp;&nbsp;{next}')

def maps(request):
    type = request.GET.get('type', 'hybrid')
    lat = request.GET.get('lat', '13.7245601')
    lon = request.GET.get('lon', '100.4930241')
    zoom = request.GET.get('z', 11)

    return HttpResponse(f"Map type: {type} <br> \
                        Location: {lat}, {lon} <br> \
                        Zoom: {zoom}")