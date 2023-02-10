from django.shortcuts import render

from .models import *


def index_page(request):
    context = {}
    cabinet = Cabinet.objects.all()
    context['cab'] = cabinet

    return render(request, 'index.html', context)

def cabinet_page(request, num):

    context = {}
    cabinet = Cabinet.objects.get(id=num)
    context['data'] = cabinet

    print(cabinet)

    return render(request, 'cabinet.html', context)

def admin_page(request):
    context = {}

    cabinet = Cabinet.objects.all()
    context['cab'] = cabinet

    return render(request, 'admin.html', context)

def addcabinet_page(request):
    context = {}

    if request.method == "POST":


        d = True

        s = request.POST['danger']

        if s == 'Опасный кабинет':
            d = True

        elif s == 'Обычный кабинет':
            d = False


        cabinet = ListCabinet.objects.create(
            name = request.POST['name'],
            number = request.POST['number'],
            danger = d,
        )

        cabinet.save()

    print(request.POST)


    return render(request, 'addcabinet.html', context)

