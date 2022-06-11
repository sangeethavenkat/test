from django.shortcuts import render, redirect
from . models import *
from django.db import IntegrityError
from django.contrib import messages
from projectmanager.models import *
from django.core.mail import send_mail
from django.conf import settings
from employee.models import *
import random


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        jobtitle = request.POST['jobtitle']
        password = request.POST['password']
        try:
            u = access()
            u.name = name
            u.username = username
            u.email = email
            u.contact = contact
            u.jobtitle = jobtitle
            u.password = password
            u.save()
            messages.info(request, 'successfully created')
            return redirect('/')
        except IntegrityError as e:
            messages.info(request, 'name already exists')
            return redirect('/register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username=='admin' and password=='admin':
                messages.info(request, 'welcome')
                request.session['ad'] = username
                return redirect('/show')
        else:
            messages.info(request, 'invalid login')
            return redirect('/login')
    else:
        return render(request, 'admins/loginadmin.html')


def show(request):
    return render(request, 'admins/AdminAccess.html')

def document(request):
    st=emp.objects.filter(status='new',empid__isnull=True)
    return render(request,'admins/generateid.html',{'st':st})

def distribute(request,id):
    st=emp.objects.get(id=id)
    r=random.randint(1000,2000)
    st.empid=r
    st.save()
    at = emp.objects.filter(id=id)
    subject = "resource"
    msg = "ID has been generated"
    to = [at[0].email]
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
    if res == 1:
        messages.info(request, "Mail Sent Successfully")
    else:
        messages.info(request, "sorry,could not send mail ")
    return redirect('/document/')
def sendid(request):
    st=emp.objects.filter(status='new',send=False)
    return render(request,'admins/sendtopm.html',{'st':st})


def moveid(request,id):
    st=emp.objects.get(id=id)
    st.send=True
    st.save()
    messages.info(request, 'sending files to project manager')
    return redirect('/sendid/')


def displayemp(request):
    st = adminpm.objects.filter(approve=False)
    return render(request, 'admins/AdminAccessTable.html', {'st': st})


def approved(request,username):
    st = adminpm.objects.get(username=username)
    st.approve = True
    st.save()
    messages.info(request, 'project manager approved')
    return redirect('/display/')


def viewpm(request):
    st = adminpm.objects.all()
    s = []
    for i in range(len(st)):
        if st[i].approve != 0:
            s.append(st[i])
    messages.info(request,'approved manager details')
    return render(request, 'admins/AdminAccessTable1.html', {'st': s})


def showresource(request):
    st = resources.objects.filter(status='Allocated',sent=False)
    return render(request, 'admins/AdminResourceTable.html', {'st': st})


def mail(request, tlname, pmname):
    ap = adminpm.objects.filter(name=pmname)
    at = accesstl.objects.filter(name=tlname)
    subject = "resource"
    msg = "requested resource is allocated"
    to = [ap[0].email, at[0].email]
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
    if res == 1:
        messages.info(request, "Mail Sent Successfully")
    else:
        messages.info(request, "sorry,could not send mail ")

    return redirect('/showresource')


def finished(request,id):
    st=resources.objects.get(id=id)
    st.sent=True
    st.save()
    return redirect('/showresource')


def logout(request):
    del request.session['ad']
    return redirect('/')
