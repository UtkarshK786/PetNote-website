from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pets
from django.db.models import Q #for or (|) in search otherwise no need
# Create your views here.
def home(req):
          pets=Pets.objects.all()
          return render(req,'home.html',{'pets':pets})

def search(req):
          srch=req.GET['srch']
          result=Pets.objects.filter(Q(petname__icontains=srch) | Q(category__icontains=srch ))
          return render(req,'home.html',{'pets':result})
def price_filter(req):
        fltr=req.GET.get('fltr')
        print(fltr)
        if fltr=='5000':
         result=Pets.objects.filter(price__lte=5000)
         result=result.order_by('price')
         return render(req,'home.html',{'pets':result})
        elif fltr=='10000':
         result=Pets.objects.filter(Q(price__gte=5000),Q(price__lte=10000))
         result=result.order_by('price')
         return render(req,'home.html',{'pets':result})
        elif fltr=='15000':
         result=Pets.objects.filter(Q(price__gte=10000),Q(price__lte=15000))
         result=result.order_by('price')
         return render(req,'home.html',{'pets':result})
        elif fltr=='20000':
         result=Pets.objects.filter(price__gte=15000)
         return render(req,'home.html',{'pets':result}) 
        return render(req,'home.html')

def about(req):
         return render(req,'about.html')

def contact(req):
         return render(req,'contact.html')
