from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.

def index(request):
    respone = HttpResponse()
    respone.writelines("This is a page of product")
    return respone

def test_product(request):
    respone  = HttpResponse()
    respone.writelines("<h1>Test product</h1>")
    return respone