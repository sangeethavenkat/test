from django.shortcuts import render,redirect
from . models import *
from django.db import IntegrityError
from projectmanager.models import *
from employee.models import *
from admins.models import *
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        platform=request.POST['platform']
        password = request.POST['password']
        try:
            u = accesstl()
            u.name=name
            u.username = username
            u.email = email
            u.contact = contact
            u.platform=platform
            u.password = password

            u.save()
            messages.info(request,"successfully created")
            return redirect('/tl/login')
        except IntegrityError as e:
            messages.info(request,"name already exists")
            return redirect('/tl/register1')
    return render(request,'teamleader/register1.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            r=accesstl.objects.get(username=username,password=password,approved=1)
            request.session['tl']=r.name
            request.session['team']=r.platform
            messages.info(request,"Welcome")
            return redirect('/tl/show')
        except accesstl.DoesNotExist as e:
            messages.info(request, 'Login access after manager approves')
            return redirect('/tl/login')
    else:
        return render(request,'teamleader/login.html')


def show(request):
    return render(request,'teamleader/TlAccess.html')


def newemp(request):
    st=emp.objects.filter(tl=request.session['tl'],status='new',team='new')
    return render(request,'teamleader/newemployee.html',{'st':st})


def provideteam(request,id):
    st=emp.objects.get(id=id)
    st.team=request.session['team']
    st.save()
    messages.info(request,'Allocated Team to New Employee')
    return redirect('/tl/newemp/')


def displayemp(request):
    st=emp.objects.filter(team=request.session['team'])
    messages.info(request,'Working Employee Details')
    return render(request,'teamleader/TlAccessTable.html',{'st':st})


def allocated(request):
    if request.method == 'POST':
        employeename=request.POST['employeename']
        work = request.POST['work']
        duedays = request.POST['duedays']
        status="pending"
        u = allocation()
        u.employeename=employeename
        u.work=work
        u.duedays=duedays
        u.status=status
        u.save()
        messages.info(request, "Work Allocated")
        return redirect('/tl/show')
    return render(request,'teamleader/TlAllocate.html')


def viewwork(request):
    st = allocation.objects.all()
    return render(request, 'teamleader/TlAccessAllocateTable.html', {'st': st})


def resource(request):
    if request.method == 'POST':
        pmname=request.POST['pmname']
        resourcename = request.POST['resourcename']
        need = request.POST['need']
        nameofproject=request.POST['projectname']
        onoroff = request.POST['onoroff']
        duedays = request.POST['duedays']
        status="Not Allocated"
        u = resources()
        u.tlname = request.session['tl']
        u.pmname = pmname
        u.resourcename = resourcename
        u.need = need
        u.projectname=nameofproject
        u.onoroff = onoroff
        u.duedays = duedays
        u.status=status
        u.save()
        messages.info(request, "Resources Requested")

    st=adminpm.objects.filter(approve=True)
    return render(request,'teamleader/TlResource.html',{'st':st})


def myresource(request):
    st=resources.objects.filter(tlname=request.session['tl'])
    s=[]
    for i in range(len(st)):
        if st[i].status == "Not Allocated":
            s.append(st[i])
    return render(request, 'teamleader/myresource.html', {'st': s})


def logout(request):
    del request.session['tl']
    return redirect('/')








