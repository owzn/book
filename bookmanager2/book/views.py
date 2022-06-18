from django.http import HttpResponse
from django.shortcuts import render

from book.models import BookInfo


# Create your views here.
def index(request):
    return HttpResponse("index")
