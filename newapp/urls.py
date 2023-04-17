from django.urls import path

from . import views

app_name='newapp'

urlpatterns = [

    path('', views.department, name='department'),
    path('add', views.CreateView, name='add'),
    path('<int:pk>/', views.UpdateView, name='change'),
]
