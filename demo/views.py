import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')

def time(request):
    feature = datetime.datetime.now().time()
    return HttpResponse(f'Time = {feature}')

