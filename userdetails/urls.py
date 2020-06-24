from django.urls import path, include

from .views import login_page, register_new
from .views import *

urlpatterns = [
    path('', login_page),
    path('register', register_new),
    path('login/', login_page, name='login_page'),
    path('passwordreset/', change_password),
    path('logout/', logout_page)
]