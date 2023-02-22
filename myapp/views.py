from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
import uuid
import datetime
from datetime import timedelta

# Create your views here.
def intex(request):
    return render(request, 'intex.html')

# def login(request):
#     if request.method=='POST':
#         a=logform(request.POST)
#         if a.is_valid():
#             nm=a.cleaned_data["name"]
#             em=a.cleaned_data["email"]
#             ps=a.cleaned_data["password"]
#             b=regmodel.objects.all()   #fetchall
#             for i in b:
#                 if nm==i.name and ps==i.password:
#                     return render(request, 'user profile.html')
#                     # return HttpResponse("Login Success")
#             else:
#                 return HttpResponse("Login Failed")
#     return render(request,'user login.html')

def login(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            unm=a.cleaned_data["username"]
            em=a.cleaned_data["email"]
            ps=a.cleaned_data["password"]
            b=regmodel.objects.all()   #fetchall
            for i in b:
                if unm==i.username and ps==i.password and em==i.email:
                    # return redirect(userprofile)
                    return render(request, 'user profile.html')
                    # return HttpResponse("Login Success")
            else:
                return HttpResponse("Login Failed")
    return render(request,'user login.html')

def display(request):
    a = regmodel.objects.all()
    return render(request, 'display.html', {'a': a})


# def register(request):
#     if request.method == 'POST':
#         a = regform(request.POST)
#         if a.is_valid():
#             # is_valid()-->is a function that is used to check the validity of form fiels.  #cleaned_data:valid forms fields are known as cleaned_data.
#             nm = a.cleaned_data["name"]
#             em = a.cleaned_data["email"]
#             pn = a.cleaned_data["phone"]
#             add = a.cleaned_data["address"]
#             pin = a.cleaned_data["pincode"]
#             ps = a.cleaned_data["password"]
#             cp = a.cleaned_data["confirm_password"]
#             if ps == cp:
#                 b = regmodel(name=nm, email=em, phone=pn, address=add, pincode=pin, password=ps)
#                 b.save()
#                 return redirect(login)
#                 # return HttpResponse("Registeration Success")
#             else:
#                 return HttpResponse("Password doesn't Match")
#         else:
#             return HttpResponse("Registeration failed")
#     return render(request, 'user register.html')

def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            # is_valid()-->is a function that is used to check the validity of form fiels.  #cleaned_data:valid forms fields are known as cleaned_data.
            unm = a.cleaned_data["username"]
            fn=a.cleaned_data["first_name"]
            lsn=a.cleaned_data["last_name"]
            em= a.cleaned_data["email"]
            ps = a.cleaned_data["password"]
            cp = a.cleaned_data["confirm_password"]
            if ps == cp:
                b = regmodel(username=unm,first_name=fn,last_name=lsn, email=em,password=ps)
                b.save()
                return redirect(login)
                # return HttpResponse("Registeration Success")
            else:
                return HttpResponse("Password doesn't Match")
        else:
            return HttpResponse("Registeration failed")
    return render(request, 'user register.html')

def shoplogin(request):
    if request.method=='POST':
        a=logsellerform(request.POST)
        if a.is_valid():
            snm=a.cleaned_data["sname"]
            em=a.cleaned_data["email"]
            ps=a.cleaned_data["password"]
            request.session["shopname"]=snm    #to make a variable global
            b=regsellermodel.objects.all()   #fetchall
            for i in b:
                if snm==i.sname and ps==i.password and em==i.email:
                    request.session['id']=i.id
                    return redirect(sellerprofile)
            else:
                return HttpResponse("Login Failed")
    return render(request, 'shop login.html')


def shopregister(request):
    if request.method == 'POST':
        b = regsellerform(request.POST)
        if b.is_valid():
            snm = b.cleaned_data["sname"]
            add = b.cleaned_data["address"]
            em = b.cleaned_data["email"]
            pn = b.cleaned_data["phone"]
            pin =b.cleaned_data["pincode"]
            ps = b.cleaned_data["password"]
            cp = b.cleaned_data["confirm_password"]
            if ps == cp:
                b = regsellermodel(sname=snm,address=add, email=em, phone=pn, pincode=pin, password=ps)
                b.save()
                return redirect(shoplogin)
                # return render(request,'shop login.html')
            else:
                return HttpResponse("Password doesn't Match")
        else:
            return HttpResponse("Registeration failed")
    return render(request, 'Shop register.html')

def sellerdisplay(request):
    a = regsellermodel.objects.all()
    return render(request, 'sellerdisplay.html', {'a': a})

def sellerprofile(request):
    shopname=request.session["shopname"]
    return render(request,'seller profile.html',{"shopname":shopname})

def userprofile(request):
    username=request.session['username']
    return render(request,'user profile.html',{'username':username})

def fileupload(request):
    if request.method=='POST':
        a=fileform(request.POST,request.FILES)
        id=request.session['id']
        if a.is_valid():
            pn=a.cleaned_data['pname']
            pp=a.cleaned_data['pprize']
            pd=a.cleaned_data['pdes']
            pimg=a.cleaned_data['pimage']
            b=filemodel(shopid=id,pname=pn,pprize=pp,pdes=pd,pimage=pimg)
            b.save()
            return redirect(filedisplay)
            # return HttpResponse("Uploaded successfully")
        else:
            return HttpResponse("Upload Failed")
    return render(request,'file upload.html')

def filedisplay(request):
    shopid=request.session['id']
    a=filemodel.objects.all()
    image=[]
    name=[]
    prize=[]
    description=[]
    id=[]
    shopid=[]
    for i in a:
        sid=i.shopid
        shopid.append(sid)
        id1=i.id
        id.append(id1)
        pimg=i.pimage
        image.append(str(pimg).split('/')[-1])
        pn=i.pname
        name.append(pn)
        pp=i.pprize
        prize.append(pp)
        pd=i.pdes
        description.append(pd)
    mylist=zip(image,name,prize,description,id,shopid)
    return render(request,'file display.html',{'mylist':mylist,'shopid':shopid})


#models.objects.get(id=id)
#what is crud? create,read,update,delete
def filedelete(request,id):
    a=filemodel.objects.get(id=id)
    a.delete()
    return redirect(filedisplay)

def fileedit(request,id):
    a=filemodel.objects.get(id=id)
    im=str(a.pimage).split('/')[-1]
    if request.method=="POST":
        if len(request.FILES):      #to check the new file
            if len(a.pimage)>0:     #to check if there is old image file.
                os.remove(a.pimage.path)   #removing the path of old file.
            a.pimage=request.FILES['pimage']  #replacing with new image.
        a.pname=request.POST.get('productname')
        a.pprize=request.POST.get('productprize')
        a.pdes=request.POST.get('des')
        a.save()
        return redirect(filedisplay)
    return render(request,'file edit.html',{'a':a,'im':im})

def registeration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        #checking wheather the user name exist
        if User.objects.filter(username=username).first():    #the filter method is used to filter the search and allows you to return only the rows that matches the search term.
            #first-->it will get first object from the filter query.
            messages.success(request,'Username Already Taken')
            #message.success is a framework that allows you to store messages in one request and retrive them in the request page.
            return redirect(registeration)
        if User.objects.filter(email=email).first():
            messages.success(request,'Email Already Exist')
            return redirect(registeration)
        user_obj=User(username=username,email=email,first_name=first_name,last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()

        #uuid module-->uuid that stands for universally unique identifiers
        #uuid4 is a function that creates random uuid.
        #import uuid-->type ta pagestart
        auth_token=str(uuid.uuid4()) #-->it generates random tokens
        #new model is created
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        #user defined
        send_mail_registeration(email,auth_token)  #mail sending fonction and it is user defined
        return render(request,'Registeration completed successfully.html')
    return render(request,'customer registeration.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username']=username
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'User not found')
            return redirect(userlogin)
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'Profile not verified check your mail')
            return redirect(userlogin)
        user=authenticate(username=username,password=password)
        #user=valid
        #if the given credentials are valid,return a user object.
        if user is None:
            messages.success(request,'Wrong password or username')
            return redirect(userlogin)
        return redirect(userprofile)
        #return HttpResponse("Success")
    return render(request,'user login.html')


#send_mail(subject, message, from_email, recipient_list
def send_mail_registeration(email,auth_token):
    subject="Your Account has been Verified"
    message=f'Click the link to verify your Account http://127.0.0.1:8000/myapp/verify/{auth_token}'
    #f is a string literal which contains expression inside curly bracets the exprssions are replaced by values.
    email_from=EMAIL_HOST_USER  #from
    recipient=[email] #to
    send_mail(subject,message,email_from,recipient)   #inbuild function

def verify(request,auth_token):
       profile_obj=profile.objects.filter(auth_token=auth_token).first()
       if profile_obj:
           if profile_obj.is_verified:
               messages.success(request,'Your account is already verified')
               return redirect(userlogin)
           profile_obj.is_verified=True
           profile_obj.save()
           messages.success(request,'Your account has been verified')
           return redirect(userlogin)
       else:
           messages.success(request,'User not found')
           return redirect(userlogin)

def filedisplayuser(request):
    a=filemodel.objects.all()
    image=[]
    name=[]
    prize=[]
    description=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        pimg=i.pimage
        image.append(str(pimg).split('/')[-1])
        pn=i.pname
        name.append(pn)
        pp=i.pprize
        prize.append(pp)
        pd=i.pdes
        description.append(pd)
    mylist=zip(image,name,prize,description,id)
    return render(request,'file display user.html',{'mylist':mylist})

def addtocart(request,id):
    a=filemodel.objects.get(id=id)
    b=cart(pname=a.pname,pprize=a.pprize,pdes=a.pdes,pimage=a.pimage)
    b.save()
    # return HttpResponse("Item added Successfully")
    # return render(request,'add to cart.html')
    return redirect(cartdisplay)

def cartdisplay(request):
    a = cart.objects.all()
    image = []
    name = []
    prize = []
    description = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        pimg = i.pimage
        image.append(str(pimg).split('/')[-1])
        pn = i.pname
        name.append(pn)
        pp = i.pprize
        prize.append(pp)
        pd = i.pdes
        description.append(pd)
    mylist = zip(image, name, prize, description, id)
    return render(request, 'cart.html', {'mylist': mylist})


def addtowishlist(request,id):
    a=filemodel.objects.get(id=id)
    b=wishlist(pname=a.pname,pprize=a.pprize,pdes=a.pdes,pimage=a.pimage)
    b.save()
    return redirect(wishlistdisplay)
    # return render(request,'wishlist.html')
    # return HttpResponse("Added")

def addcartwishlist(request,id):
    a=wishlist.objects.get(id=id)
    b=cart(pname=a.pname,pprize=a.pprize,pdes=a.pdes,pimage=a.pimage)
    b.save()
    return redirect(cartdisplay)

def wishlistdisplay(request):
    a = wishlist.objects.all()
    image = []
    name = []
    prize = []
    description = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        pimg = i.pimage
        image.append(str(pimg).split('/')[-1])
        pn = i.pname
        name.append(pn)
        pp = i.pprize
        prize.append(pp)
        pd = i.pdes
        description.append(pd)
    mylist = zip(image, name, prize, description, id)
    return render(request, 'wishlist.html', {'mylist': mylist})

def removecart(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)

def removewishlist(request,id):
    a=wishlist.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)

def cartbuy(request,id):
    a=cart.objects.get(id=id)
    image=str(a.pimage).split('/')[-1]
    if request.method=='POST':
        name=request.POST.get('pname')
        des=request.POST.get('pdes')
        quantity1=request.POST.get('quantity')
        price1=request.POST.get('price')
        b=buy1(pname=name,pdes=des,quantity=quantity1,pprize=price1)
        b.save()
        total=int(price1)*int(quantity1)
        return render(request,'finalbill.html',{'total':total,'name':name,'quantity':quantity1})
    return render(request,'quantity selection.html',{'a':a})


def cardpayment(request):
    if request.method=='POST':
        cardname=request.POST.get('cardname')
        cardnumber= request.POST.get('cardnumber')
        cardexpiry= request.POST.get('cardexpiry')
        securitycode= request.POST.get('securitycode')
        user_obj=customercard(cardname=cardname,cardnumber=cardnumber,cardexpiry=cardexpiry,securitycode=securitycode)
        user_obj.save()
        # a=datetime.date.today()
        # b=a+timedelta(15)
        # print(b)
        return render(request,'orderstatus.html')
    return render(request,'card payment.html')

def orderstatus(request):
    return render(request,'orderstatus.html')