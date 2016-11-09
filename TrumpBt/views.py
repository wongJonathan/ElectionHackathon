from django.shortcuts import render
from theButton.models import *
# Create your views here.

def random():
    quote= Quote.objects.order_by('?')

    return  quote
