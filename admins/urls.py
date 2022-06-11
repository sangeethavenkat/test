from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register),
    path('display/', views.displayemp, name='display'),
    path('show/',views.show,name='show'),
    path('login/',views.login,name='login'),
    path('approve/<str:username>',views.approved),
    path('viewpm/',views.viewpm),
    path('showresource/',views.showresource),
    path('mail/<str:tlname>/<str:pmname>',views.mail),
    path('finished/<int:id>',views.finished),
    path('document/',views.document,name='document'),
    path('distribute/<int:id>',views.distribute,name='distribute'),
    path('sendid/',views.sendid,name='sendid'),
    path('moveid/<int:id>',views.moveid,name='moveid'),
    path('logout/',views.logout)


]