from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('wheels', views.wheels, name='wheels'),
    path('wheels/<int:pk>/', views.wheelsDetail, name='wheelsdetail'),

    path('disks', views.disks, name='disks'),
    path('disks/<int:pk>/', views.disksDetail, name='disksdetail'),

    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('account', views.account, name='account'),
    path('registration', views.registration, name='regist'),
]