from django.shortcuts import render

from .models import Cabinet


def index_page(request):
    context = {}
    return render(request, 'index.html', context)

def cabinet_page(request):
    # context = {}
    # profile = Cabinet.objects.get()
    # context['data'] = Cabinet.objects.all()

    return render(request, 'cabinet.html')