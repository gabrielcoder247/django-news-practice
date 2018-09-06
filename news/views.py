from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render

# Create your views here.

def welcome(request):
      return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    html = f''''
        <html>
            <body>
                <h1>{date.day}--{date.month}--{date.year}</h1>
            </body>
        </html>

        '''
    return HttpResponse(html) 

# def convert_dates(dates):
#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)
#     day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#     # Returning the actual day of the weekday
#     day = days[day_number]

#     return day

def past_days_news(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()





