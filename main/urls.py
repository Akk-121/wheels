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
    path('add_any', views.add_any, name='add_any'),
    path('anketa', views.anketa, name='anketa'),
    path('account', views.account, name='account'),
    path('registration', views.registration, name='regist'),

    path('socket/<int:pk>/', views.socket, name='socket'),
    path('del_socket/<int:pk>/', views.del_socket, name='del_socket'),
    path('socket', views.socket_base, name='socket_base'),

    path('order', views.order, name='order'),
]