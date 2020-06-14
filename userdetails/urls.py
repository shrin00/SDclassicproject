from django.urls import path, include

from .views import login_page, register_new

urlpatterns = [
    path('', login_page),
    path('register', register_new)
]