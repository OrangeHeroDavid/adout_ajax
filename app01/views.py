from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
@ensure_csrf_cookie
def index(request):
    i1 = request.POST.get('i1', '')
    i2 = request.POST.get('i2', '')

    i3 = int(i1) + int(i2) if i1 and i2 else ''

    return render(request, 'index.html', {'i1': i1, 'i2': i2, 'i3': i3})


import time


def calc(request):
    i1 = request.POST.get('i1', '')
    i2 = request.POST.get('i2', '')

    time.sleep(3)

    i3 = int(i1) + int(i2) if i1 and i2 else ''
    return HttpResponse(i3)


def calc2(request):
    i1 = request.POST.get('i1', '')
    i2 = request.POST.get('i2', '')

    i3 = int(i1) + int(i2) if i1 and i2 else ''
    return HttpResponse(i3)


import json


def ajax_test(request):
    print(request.POST)
    print(request.POST.get('name'))
    print(request.POST.get('age'))
    hobby = request.POST.get('hobby')
    print(json.loads(hobby))

    # int('aaa')
    return HttpResponse('ok')


def upload(request):
    if request.is_ajax():
        file_obj = request.FILES.get('f1')
        with open(file_obj.name, 'wb')  as f:
            for i in file_obj.chunks():
                f.write(i)
        return HttpResponse('上传成功')

    return render(request, 'upload.html')
