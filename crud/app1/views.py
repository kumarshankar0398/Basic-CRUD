from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import EmployeeForm
from .models import Employee
import re
from django.db.models.functions import Lower
from django.contrib import messages


# Create your views here.
def Validation(EmpId, EmpName, EmpContact, EmpSal, EmpEmail, EmpAddress):
    if not re.match("[0-9]+", EmpId):
        if not re.match("^[-a-zA-Z\s]*$", EmpName):
            if not re.match("^[6-9]\d{9}$", EmpContact):
                if not re.match("[0-9]+", EmpSal):
                    if not re.match("/([a-zA-Z0-9]+)([\_\.\-{1}])?([a-zA-Z0-9]+)\@([a-zA-Z0-9]+)([\.])([a-zA-Z\.]+)/g",
                                    EmpEmail):
                        if not re.match("^[-a-zA-Z\s]*$", EmpAddress):
                            return False
    return False


@login_required(login_url='/')
def home(request):
    return render(request, 'app1/home.html')


@login_required(login_url='/')
def AddRec(request):
    if request.method == "POST":
        EmpId = request.POST.get('EmpId')
        EmpName = request.POST.get('EmpName')
        EmpContact = request.POST.get('EmpContact')
        EmpSal = request.POST.get('EmpSal')
        EmpEmail = request.POST.get('EmpEmail')
        EmpAddress = request.POST.get('EmpAddress')
        # if Validation(EmpId, EmpName, EmpContact, EmpSal, EmpEmail, EmpAddress):
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpContact=EmpContact, EmpSal=EmpSal, EmpEmail=EmpEmail,
                        EmpAddress=EmpAddress)
        data.save()
        return redirect("/ShowRec")
    return render(request, 'app1/AddRec.html')


def AddRec1(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'app1/Add1.html', {'form': form})


@login_required(login_url='/')
def ShowRec1(request):
    emp = Employee.objects.all()
    p = Paginator(emp, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


@login_required(login_url='/')
def EditRec(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'app1/EditRec.html', {'employee': employee})


@login_required(login_url='/')
def UpdateRec(request, id):
    employee = Employee.objects.get(id=id)
    emp = Employee.objects.all()
    if request.method == "POST":
        employee.EmpId = request.POST.get('EmpId')
        employee.EmpName = request.POST.get('EmpName')
        employee.EmpContact = request.POST.get('EmpContact')
        employee.EmpSal = request.POST.get('EmpSal')
        employee.EmpEmail = request.POST.get('EmpEmail')
        employee.EmpAddress = request.POST.get('EmpAddress')
        employee.save()
        return redirect("/ShowRec")
    return render(request, 'app1/EditRec.html', {'employee': employee, 'emp': emp})


@login_required(login_url='/')
def DeleteRec(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect("/ShowRec")
    return render(request, 'app1/DeleteRec.html')


@login_required(login_url='/')
def ShowRec(request):
    all_members = Employee.objects.all()
    return render(request, 'app1/ShowRec.html', {'all_members': all_members})


@login_required(login_url='/')
def SearchRec(request):
    if request.method == "POST":
        searchrec = request.POST.get('EmpName')
        emp = Employee.objects.filter(EmpName=searchrec)
        return render(request, 'app1/SearchRec.html', {'emp': emp})
    return render(request, 'app1/SearchRec.html')


@login_required(login_url='/')
def SortRecByEmpName(request):
    emp = Employee.objects.all().order_by(Lower('EmpName'))
    p = Paginator(emp, 11)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


@login_required(login_url='/')
def SortRecByEmpId(request):
    emp = Employee.objects.all().order_by('-EmpId')
    p = Paginator(emp, 11)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


@login_required(login_url='/')
def SortRecByEmpContact(request):
    emp = Employee.objects.all().order_by('-EmpContact')
    p = Paginator(emp, 11)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


@login_required(login_url='/')
def SortRecByEmpSal(request):
    emp = Employee.objects.all().order_by('-EmpSal')
    p = Paginator(emp, 11)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


@login_required(login_url='/')
def SortRecByEmpEmail(request):
    emp = Employee.objects.all().order_by('-EmpEmail')
    p = Paginator(emp, 11)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


@login_required(login_url='/')
def SortRecByEmpAddress(request):
    emp = Employee.objects.all().order_by(Lower('EmpAddress'))
    p = Paginator(emp, 11)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'emp': emp}
    return render(request, 'app1/ShowRec1.html', context)


# def signup(request):
#     if request.method == "POST":
#         passwd1 = request.POST['password1']
#         passwd2 = request.POST['password2']
#         usrname = request.POST['username']
#         email = request.POST['email']
#         if passwd1 == passwd2:
#             try:
#                 User.objects.get(username=usrname)
#                 return render(request, 'app1/registration.html', {'error': 'Username is already taken!'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(username=usrname, password=passwd1, email=email)
#                 login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'app1/registration.html', {'error': 'Password does not match!'})
#     return render(request, 'app1/registration.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print("User created")
                return redirect('/')
        else:
            messages.info(request, 'password not matching...')
            return redirect('/signup')
    else:
        return render(request, 'app1/registration.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user)
            request.session['username'] = username
            request.session.set_expiry(300)
            return redirect('/home')
        else:
            return render(request, 'app1/login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'app1/login.html')


@login_required(login_url='/')
def logout_user(request):
    logout(request)
    print(request.user)
    return redirect('/')

# @login_required(login_url='/')
# def logout_user(request):
#     try:
#         del request.session['username']
#     except KeyError:
#         pass
#     #return HttpResponse("You're logged out.")
#     return redirect('/')
