from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(req):
           if req.method=='POST': 
                fn=req.POST['fn'] 
                ln=req.POST['ln'] 
                eml=req.POST['eml'] 
                mbl=req.POST['mbl'] 
                pwd1=req.POST['pwd1'] 
                pwd2=req.POST['pwd2']
                if len(fn)<1 or len(ln)<1 or len(eml)<1 or len(mbl)<1 or len(eml)<1 or len(pwd1)<1 or len(pwd2)<1:
                  messages.info(req,'please fill all the fields')
                  return render(req,'register.html')
                elif len(mbl)!=10:
                    messages.info(req,'please enter a vaid mobile number')
                    return render(req,'register.html')
                elif pwd1!=pwd2:
                    messages.info(req,'passwords are not matching')
                    return render(req,'register.html')
                else:
                  user=User.objects.create_user(first_name=fn,last_name=ln,email=mbl,username=eml,password=pwd1)
                  user.save()
                return render(req,'login.html')
            
           else:
               return render(req,'register.html')
def login(req):
          if req.method=='POST':
               eml=req.POST['eml']
               pwd=req.POST['pwd']
               user=auth.authenticate(username=eml,password=pwd)
               if user is not None:
                 auth.login(req,user)
                 return redirect('/')
               else:
                 messages.info(req,'invalid credentials')
                 return render(req,'login.html')
          return render(req,'login.html')
       
def logout(req):
       auth.logout(req)
       return redirect('/')
             
