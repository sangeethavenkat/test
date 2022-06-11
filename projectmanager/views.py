from django.shortcuts import render, redirect
from . models import *
from django.db import IntegrityError
from admins.models import *
from teamleader.models import *
from sklearn import preprocessing
from sklearn.svm import SVC
import pandas as pd
from django.contrib import messages
from employee.models import *



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
            u = adminpm()
            u.name = name
            u.username = username
            u.email = email
            u.contact = contact
            u.jobtitle = jobtitle
            u.password = password
            u.save()
            messages.info(request,"successfully created")
            return redirect('/pm/login')
        except IntegrityError as e:
            messages.info(request,"name already exists")
            return redirect('/pm/registerpm')
    return render(request, 'manager/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            r=adminpm.objects.get(username=username, password=password)
            request.session['mng'] = r.name
            print(r.name)
            if r.approve == 1:
                messages.info(request,'login successful')
                return redirect('/pm/show')
            else:
                messages.info(request,'Login access after admin approves')
                return redirect('/pm/login')
        except adminpm.DoesNotExist as e:
            print("error")
            return redirect('/pm/login')
    else:
        return render(request, 'manager/login.html')


def show(request):
    return render(request, 'manager/PmAccess.html')



def displayemp(request):
    st=accesstl.objects.filter(approved=False)
    return render(request, 'manager/PmAccessTable.html', {'st': st})


def approved(request,id):
    st = accesstl.objects.get(id=id)
    st.approved = True
    st.save()
    return redirect('/pm/display1/')


def projects(request):
    st=emp.objects.filter(status='new',project__isnull=True)
    at=accesstl.objects.all()
    return render(request,'manager/projectallocate.html',{'st':st,'at':at})


def impart(request,id):
    if request.method=='POST':
        project=request.POST['project']
        tl=request.POST['tl']
        st=emp.objects.get(id=id)
        st.project=project
        st.tl=tl
        st.save()
    return redirect('/pm/projects/')


def status(request):
    st=allocation.objects.all()
    return render(request, 'manager/ProjectStatus.html', {'st': st})


def showresource(request):
    st=resources.objects.filter(pmname=request.session['mng'], status='Not Allocated')
    return render(request, 'manager/PmResourceTable.html', {'st': st})


def algo(request,id):
    st = resources.objects.get(id=id)
    d ={'on-going':1,'off-going':2}
    data_set = pd.read_csv('data.csv')
    le = preprocessing.LabelEncoder()
    x = data_set.iloc[:, [0, 1]].values
    y = data_set.iloc[:, 2].values
    y=le.fit_transform(y)
    print(y)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(x, y)
    y_pred = svclassifier.predict([[d[st.onoroff],st.duedays]])
    a=le.inverse_transform(y_pred)
    print(a)
    resources.objects.filter(id=id).update(priority=a[0])
    return redirect('/pm/showresource')


def finished(request, id):
    resources.objects.filter(id=id).update(status="Allocated")
    return redirect('/pm/showresource')


def logout(request):
    del request.session['mng']
    return redirect('/')



