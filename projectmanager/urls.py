from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register1/',views.register),
    path('login/',views.login,name='login'),
    path('display1/', views.displayemp, name='display1'),
    path('show/', views.show, name='show'),
    path('status/', views.status),
    path('approved/<int:id>', views.approved),
    path('showresource/',views.showresource),
    path('finished/<int:id>',views.finished),
    path('projects/',views.projects,name='projects'),
    path('impart/<int:id>',views.impart,name='impart'),
    path('algo/<int:id>', views.algo),
    path('logout/',views.logout)

  ]