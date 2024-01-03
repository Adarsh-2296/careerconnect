from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import std, dep, proeditstd1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def print_hello(request):
    if request.POST:
        FullName=request.POST.get('name')
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        PhoneNumber=request.POST.get('PhoneNumber')
        YearofCollege=request.POST.get('collegeYear')
        department=request.POST.get('department')
        reg_obj=std(FullName=FullName, Email=Email, Password=Password, PhoneNumber=PhoneNumber, YearofCollege=YearofCollege, department=department)
        reg_obj.save()
        return redirect('studentpro')

    return render(request, 'student-register.html')
    

def alulogin(request):
    return render(request, 'alulogin.html')

def alumnipro(request):
    return render(request, 'alumnipro.html')

def alumniproedit(request):
    return render(request, 'alumniproedit.html')

def deptlogin(request):
    if request.POST:
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        dep_obj=dep(Email=Email, Password=Password)
        dep_obj.save

    return render(request, 'deptlogin.html')

def main(request):
    return render(request, 'main.html')

def login(request):
    if request.POST:
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        
        reg_obj = authenticate(Email=Email, Password=Password )
        if reg_obj is not None:
            login(request, reg_obj)
            
            return render(request='studentpro.html')
        else:
            messages.error(request, "Bad Credentials")
    return render(request, 'login.html')
    
    


def studentpro(request):
    return render(request, 'studentpro.html')

def forgotps(request):
    return render(request,'forgotps.html')

def stdproedit(request):
    if request.POST:
        img=request.FILES.get('img')
        experience=request.POST.get('experience')
        skills=request.POST.get('skills')
        internships=request.POST.get('internships')
        workDone=request.POST.get('workDone')
        workDetails=request.POST.get('workDetails')
        hobbies=request.POST.get('hobbies')
        achievements=request.POST.get('achievements')
        proeditstd_obj=proeditstd1(experience=experience, skills=skills, internships=internships, workDone=workDone, workDetails=workDetails, hobbies=hobbies, achievements=achievements, img=img)
        proeditstd_obj.save()
        return redirect('studentpro')
        
    return render(request,'stdproedit.html')




        
