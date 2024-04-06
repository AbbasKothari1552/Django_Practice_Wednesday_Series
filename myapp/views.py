from django.shortcuts import render,redirect


import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.


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
