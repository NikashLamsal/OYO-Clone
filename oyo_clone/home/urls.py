from django.urls import path
from home.views import *

urlpatterns = [
    path("",index,name = "index"),
    path("login/",login,name = "login_page"),
    path("register/",register,name = "register_page")

]
