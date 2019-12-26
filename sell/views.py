from django.shortcuts import render
from petnote.models import Pets
from django.contrib import messages

# Create your views here.
def post(req):
       if req.method=='POST':
             pet=Pets()
             petname=req.POST['petname']
             category=req.POST['category']
             price=req.POST['price']
             img=req.POST['img']
             if len(petname)<1 or len(category)<1 or len(price)<1 or len(img)<1:
               messages.info(req,"Please fill all the fields")
               return render(req,'sell.html')
             else:
               pet.petname=petname
               pet.category=category
               pet.price=price
               img='pics/'+img
               pet.img=img
               pet.save()
               msg="Successfully posted"
               return render(req,'sell.html',{'msg':msg})
                        
       return render(req,'sell.html')
