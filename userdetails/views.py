from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, request
from .models import details

#User=get_user_model()
def login_page(request):
    data={"invalid":False}
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/manageing/home/')
        else:
            try:
                u = User.objects.get(username=email)
                data = {"invalid": True, 'email': email, 'user': u}
            except User.DoesNotExist:
                u = None
                data={"invalid":True, 'email':email, 'user':u}
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
        # print('ji', user)
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

def change_password(request):
    data={'exists':False}
    email= request.POST.get('email')
    newpassword = request.POST.get('newpassword')
    if email:
        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            user=None

        if user is not None:
            user.set_password(newpassword)
            user.save()
            print('password has been changed !')
            return redirect('/userdetails/login/')
        else:
            data['exists']= True
            data['email'] = email
            print(data)

    return render(request, 'userdetails/passwordrest.html', data)

def logout_page(request):
    if request.user.is_authenticated:
        print('loged out!')
        logout(request)
    return redirect('login_page')