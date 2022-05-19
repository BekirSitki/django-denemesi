from re import template
from django.shortcuts import render
from matplotlib.style import context
from requests import request
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Notlar
from django.urls import reverse

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    notlar = Notlar.objects.all().values()
    context = { 
        'notlar':notlar,
    }


    return HttpResponse(template.render(context,request))

def ekle(request):
    template = loader.get_template('ekle.html')
    return HttpResponse(template.render({}, request))

def notekle(request):
    eklenecek_baslik = request.POST['baslik']
    eklenecek_icerik = request.POST['icerik']
    ekle = Notlar(baslik = eklenecek_baslik, icerik = eklenecek_icerik)
    ekle.save()
    return HttpResponseRedirect(reverse('index'))
 
def sil(request, id):
    silinecek_not = Notlar.objects.get(id=id)
    silinecek_not.delete()
    #
    #for bos_yer in Notlar.objects:
    #    if bos_yer.id is 1:
    #
    #        pass
    #    pass
    
    return HttpResponseRedirect(reverse('index'))

def duzenle(request, id):
    duzenlenecek_not = Notlar.objects.get(id=id)
    template = loader.get_template('duzenle.html')
    context = {
        'notlar':duzenlenecek_not,
    }
    return HttpResponse(template.render(context, request))

def notuduzenle(request, id):
    duzenlenecek_baslik = request.POST['baslik']
    duzenlenecek_icerik = request.POST['icerik']
    duzenle = Notlar.objects.get(id=id)
    duzenle.baslik = duzenlenecek_baslik
    duzenle.icerik = duzenlenecek_icerik
    duzenle.save()
    return HttpResponseRedirect(reverse('index'))