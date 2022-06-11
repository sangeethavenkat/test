from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register1/',views.register),
    path('login/',views.login,name='login'),
    path('display/', views.display, name='display'),
    path('viewwork1/',views.viewwork1),
    path('viewwork/',views.viewwork),
    path('finished/<int:id>',views.finished),
    path('newone/',views.newone,name='newone'),
    path('form/<int:id>',views.form,name='form'),
    path('logout/',views.logout)

  ]