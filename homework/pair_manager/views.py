from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Exchange, Pair

# Create your views here.

def show_exchange(request):
    exchanges = Exchange.objects.all()
    br = [str(exchange) + '<br>' for exchange in exchanges]
    return HttpResponse(br)

def add_exchange(request, name):
    Exchange.objects.create(name=name)
    return HttpResponsePermanentRedirect('/exchange/')

def delete_exchange(request, id):
    Exchange.objects.filter(id=id).delete()
    return HttpResponsePermanentRedirect('/exchange/')

def update_exchange(request, id, name):
    Exchange.objects.filter(id=id).update(name=name)
    return HttpResponsePermanentRedirect('/exchange/')

def show_pair(request):
    pairs = Pair.objects.all()
    br = [str(pair) + '<br>' for pair in pairs]
    return HttpResponse(br)

def add_pair(request, symbol, ask, bid, exchange_id):
    Pair.objects.create(symbol=symbol, ask=ask, bid=bid, exchange_id=exchange_id)
    return HttpResponsePermanentRedirect('/pair/')

def delete_pair(request, id):
    Pair.objects.filter(id=id).delete()
    return HttpResponsePermanentRedirect('/pair/')

def update_pair(request, id, symbol, ask, bid, exchange_id):
    Pair.objects.filter(id=id).update(symbol=symbol, ask=ask, bid=bid, exchange_id=exchange_id)
    return HttpResponsePermanentRedirect('/pair/')
