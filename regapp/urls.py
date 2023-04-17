from django.urls import path
from .import views

app_name='regapp'


urlpatterns = [

    path('register',views.register,name='register'),


    ]
