from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register1/',views.register),
    path('login/',views.login,name='login'),
    path('display/', views.displayemp, name='display'),
    path('show/', views.show, name='show'),
    path('newemp/',views.newemp,name='newemp'),
    path('allocate',views.allocated),
    path('forms/',views.viewwork),
    path('provideteam/<int:id>',views.provideteam,name='provideteam'),
    path('resource/',views.resource),
    path('myresource/',views.myresource),
    path('logout/',views.logout)


  ]