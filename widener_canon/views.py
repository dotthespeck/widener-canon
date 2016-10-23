from django.shortcuts import render
from django.http import HttpResponse

from .list_of_no_1 import get_list_of_composers

def index(request):
    return render(request, 'index.html')

def byno(request):
    return render(request, 'byno.html')

def no1(request):
    list_of_composers = get_list_of_composers()
    context = {'object_list': list_of_composers}
    return render(request, 'list_of_composers.html', context)


