import datetime
from django.shortcuts import render
from django.http import HttpResponse


def newyear(request):
    
    now = datetime.datetime.now()

    return render(request, 'newyear/index.html', {
        'is_newyear': now.month == 1 and now.day == 1
    })