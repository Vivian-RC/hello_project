from django.shortcuts import render
from django.http import HttpResponse

def hello_word(request):
    return HttpResponse("Hellou Word - Django no Render!")