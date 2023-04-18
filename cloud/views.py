from django.shortcuts import render

from .models import *


def index_page(request):
    context = {}
    cabinet = ListCabinet.objects.all()
    context['cab'] = cabinet

    return render(request, 'index.html', context)

def Cabinet_page(request, num):

    context = {}
    cabinet = Cabinet.objects.filter(cabinet_id=num)

    context['data'] = cabinet

    temp = [int(item.temperature) for item in cabinet[0:10]]
    context['temp'] = temp

    humidity = [int(item.humidity) for item in cabinet[0:10]]
    context['humidity'] = humidity

    lux = [int(item.lux) for item in cabinet[0:10]]
    context['lux'] = lux

    pressure = [int(item.pressure) for item in cabinet[0:10]]
    context['pressure'] = pressure


    return render(request, 'cabinet.html', context)

def admin_page(request):
    context = {}

    cabinet = ListCabinet.objects.all()
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

