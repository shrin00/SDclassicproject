from django.urls import path, include

from .views import login_page, register_new
from .views import *

urlpatterns = [
    path('', login_page),
    path('register/', register_new),
    path('login/', login_page, name='login_page'),
    path('passwordreset/', change_password),
    path('logout/', logout_page),
    path('water_dep/', water_dep),
    path('electric_dept/', electric_dept),
    path('road_dept/', road_dept),
    path('citizsenprofile/', citizsenprofile),
    path('post_news/', post_news),
    path('home_page/', load_home)
]