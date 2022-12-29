from django.shortcuts import render


def index_page(request):
    context = {}
    return render(request, 'index.html', context)

def cabinet_page(request, cabinet):
    context = {}
    profile = Cabinet.objects.get(name=cabinet)

    return render(request, 'index.html', context)