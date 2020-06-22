from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate,login,logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, request
from .models import details

#User=get_user_model()
def login_page(request):
    data={"invalid":False}
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=email, password=password)
        if user is not None:
            HttpResponse('<h1>hey! you just loged in</h1>')
        else:
            data={"invalid":True}
    return render(request, "userdetails/login.html", data)


def register_new(request):
    data={'exists':False}
    if request.POST:
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        gender=request.POST.get('gender')

        user=User.objects.filter(email=email, username=email)
        print('ji', user)

        if user.count()>0:
            data={'exists':True}
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user1 = details(
                email=email,
                first_name=fname,
                last_name=lname,
                contact=contact,
                gender=gender
            )
            user1.save()
            print(user1, user)
            return redirect('/userdetails/login/')

    return render(request, 'userdetails/register.html')