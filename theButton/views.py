from django.shortcuts import render
import re
from django.http import HttpResponse
from django.template import loader
from .models import Quote

# Create your views here.
def createQuotes():
    with open('quotes.txt','r',encoding="utf8") as f:
        data = ''.join(f.readline())

    print(data)

    phrase="Hi"
    print( re.findall('"([^"]*)"',data))
    phrase = data.split('"')

    if phrase:
        print("Phrase: True")
        for q in phrase:
            #print("Phrase: "+phrase)
            quote = Quote.objects.create(quote = q)
            quote.save()
 #   quote = Quote.objects.create(quote = "HI")
  #  quote.save()

def printQuote(request):
    #if  Quote.objects.count() == 0:
    createQuotes()
    chosenQuote = Quote.objects.order_by('?')
    template = loader.get_template('quoteDisplay.html')
    context = {
        'chosen':chosenQuote,
    }
    return HttpResponse(template.render(context,request))
