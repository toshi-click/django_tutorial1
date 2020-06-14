from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    params = {
        'title': 'Hello World',
        'msg': 'hello',
        'gopage': 'twopage'
    }
    return render(request, 'app/index.html', params)


def twopage(request):
    params = {
        'title': 'Hello World ver2',
        'msg': 'さようなら',
        'gopage': 'hello'
    }
    return render(request, 'app/index.html', params)
