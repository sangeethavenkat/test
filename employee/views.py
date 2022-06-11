from django.shortcuts import render,redirect
from . models import *
from django.db import IntegrityError
from django.contrib import messages

from teamleader.models import *


def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        team=request.POST['team']
        status=request.POST['status']
        password = request.POST['password']
        try:
            emp(name=name,username=username,email=email,contact=contact,status=status,team=team,password=password).save()
            messages.info(request,"successfully created")
            return redirect('/emp/login')
        except IntegrityError as e:
            messages.info(request,"name already exists")
            return redirect('/emp/register1')
    return render(request,'employee/registeremp.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            r=emp.objects.get(username=username,password=password)
            messages.info(request, "login successful")
            request.session['ename']=r.name
            return redirect('/emp/display')

        except emp.DoesNotExist as e:
            messages.info(request, "name does not exists")
            return redirect('/emp/login')
    else:
        return render(request,'employee/login.html')



def display(request):
    st=emp.objects.all()
    return render(request,'employee/EmployeeAccess.html',{'st':st})

def newone(request):
    st=emp.objects.filter(status='new',upload='Null')
    return render(request,'employee/documents.html',{'st':st})


def form(request,id):
    if request.method == 'POST':
        upload=request.FILES['upload']
        st=emp.objects.get(id=id)
        st.upload=upload
        st.save()
        messages.info(request,'uploaded documents successfully')
        return redirect('/emp/newone')


def viewwork1(request):
    st=allocation.objects.filter(employeename= request.session['ename'],status='pending')
    return render(request, 'employee/EmployeeTable1.html', {'st': st})


def viewwork(request):
    st=allocation.objects.filter(employeename= request.session['ename'],status='pending')
    return render(request, 'employee/EmployeeTable.html', {'st': st})


def finished(request,id):
    if request.method=='POST':
        st = allocation.objects.get(id=id)
        workstatus = request.POST[f'workstatus{st.id}']
        st.workstatus=workstatus
        st.status='finished'
        messages.info(request,'uploaded working status')
        st.save()
    return redirect('/emp/display')


def logout(request):
    del request.session['ename']
    return redirect('/')









