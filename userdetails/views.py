from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, request
from .models import details, news_update

#User=get_user_model()
def login_page(request):
    data={"invalid":False}
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            user=details.objects.filter(email=request.user.email).first()
            if user:
                if user.citizen:

                    return redirect('/userdetails/home_page/')
                elif user.water_dep:
                    return redirect('/userdetails/home_page/')
                elif user.elec_dept:
                    return redirect('/userdetails/home_page/')
                elif user.road_dept:
                    return redirect('/userdetails/home_page/')
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
                gender=gender,
                citizen=True,
                water_dep=False,
                elec_dept=False,
                road_dept=False
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

def water_dep(request):
    data = {'exists': False}
    if request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')

        user = User.objects.filter(email=email, username=email)
        # print('ji', user)
        if user.count() > 0:
            data = {'exists': True}
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user1 = details(
                email=email,
                first_name=fname,
                last_name=lname,
                contact=contact,
                gender=gender,
                citizen=False,
                water_dep=True,
                elec_dept=False,
                road_dept=False
            )
            user1.save()
            print(user1, user)
            return redirect('/userdetails/login/')

    return render(request, 'userdetails/register.html')


def electric_dept(request):
    data = {'exists': False}
    if request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')

        user = User.objects.filter(email=email, username=email)
        # print('ji', user)
        if user.count() > 0:
            data = {'exists': True}
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user1 = details(
                email=email,
                first_name=fname,
                last_name=lname,
                contact=contact,
                gender=gender,
                citizen=False,
                water_dep=False,
                elec_dept=True,
                road_dept=False
            )
            user1.save()
            print(user1, user)
            return redirect('/userdetails/login/')

    return render(request, 'userdetails/register.html')


def road_dept(request):
    data = {'exists': False}
    if request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')

        user = User.objects.filter(email=email, username=email)
        # print('ji', user)
        if user.count() > 0:
            data = {'exists': True}
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user1 = details(
                email=email,
                first_name=fname,
                last_name=lname,
                contact=contact,
                gender=gender,
                citizen=False,
                water_dep=False,
                elec_dept=False,
                road_dept=True
            )
            user1.save()
            print(user1, user)
            return redirect('/userdetails/login/')

    return render(request, 'userdetails/register.html')


def citizsenprofile(request):
    data={}
    if request.user.is_authenticated:
        us = details.objects.filter(email=request.user.email).first()
        if us.citizen:
            data={
                'fname':us.first_name,
                'lname':us.last_name,
                'email':request.user.email,
                'contact':us.contact,
                'gender':us.gender
            }
        else:
            data = {
                'fname': us.first_name,
                'lname': us.last_name,
                'email': request.user.email,
                'contact': us.contact,
                'gender': us.gender,
                'news_post':True
            }
        return render(request, 'userdetails/citizenprofile.html', data)

    else:
        return redirect('/userdetails/login/')

def post_news(request):
    data={'access':True}
    if request.user.is_authenticated:
        if request.POST:
            us = details.objects.filter(email=request.user.email).first()
            subject = request.POST.get('subject')
            news = request.POST.get('news_post')
            if us.water_dep:
                new_post = news_update(
                    subject=subject,
                    news=news,
                    water_dep=True,
                    elec_dept=False,
                    road_dept=False
                )
                new_post.save()
                return redirect('/userdetails/citizsenprofile/')
            elif us.elec_dept:
                new_post = news_update(
                    subject=subject,
                    news=news,
                    water_dep=False,
                    elec_dept=True,
                    road_dept=False
                )
                new_post.save()
                return redirect('/userdetails/citizsenprofile/')
            elif us.road_dept:
                new_post = news_update(
                    subject=subject,
                    news=news,
                    water_dep=False,
                    elec_dept=False,
                    road_dept=True
                )
                new_post.save()
                return redirect('/userdetails/citizsenprofile/')
            else:
                data={'access':True}
                return redirect('/userdetails/citizsenprofile/')
        return render(request, 'userdetails/post_news.html', data)
    else:
        return redirect('/userdetails/login/')
    
    
def load_home(request):
    data={}
    if request.user.is_authenticated:
        us = details.objects.filter(email=request.user.email).first()
        if us.citizen:
            news = news_update.objects.all()
        elif us.elec_dept:
            news = news_update.objects.filter(elec_dept=True)
        elif us.road_dept:
            news = news_update.objects.filter(road_dept=True)
        elif us.water_dep:
            news = news_update.objects.filter(water_dep=True)
        else:
            news = None
        data = {'post': news}
        return render(request, 'userdetails/home_page.html', data)
    else:
        return redirect('/userdetails/login/')