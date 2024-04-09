from django.shortcuts import render,redirect, HttpResponse
from django.template import loader


import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.

def base(request):
    return render(request, 'base.html')


def index(request,year, month):

    month = month.title()

    month_num = list(calendar.month_name).index(month)

    # create a calendar

    cal = HTMLCalendar().formatmonth(year, month_num)

    #current date & time

    now = datetime.now()

    curr_year = now.year
    curr_time = now.strftime('%H:%M %p')


    context = {
        'year' : year,
        'month' : month,
        'month_num' : month_num,
        'cal' :cal,
        'curr_year' : curr_year,
        'curr_time' :curr_time,
    }
    
    return render(request, 'index.html', context = context)

def testing(request):

    template = loader.get_template('testing.html')

    context = {
        'fruits' : ['Apple', 'Orange', 'Banana', 'Cherry'],
    }

    return HttpResponse(template.render(context, request))