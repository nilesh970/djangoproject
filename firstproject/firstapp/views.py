from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>hello good evening friends</h1>'
    msg=msg+'<h1>the current datetime is'+str(date)+'</h1>'
    return HttpResponse(msg)