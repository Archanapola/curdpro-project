from django.shortcuts import render,redirect
from .models import sdata

# Create your views here.
def mainpage(request):
    sdatade=sdata.objects.all().values()
    return render(request,'mainpage.html',{'sdatade':sdatade})




def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        sdata (
        fname=request.POST.get('fname'),
        lname=request.POST.get('lname'),
        email=request.POST.get('email'),
        mobile=request.POST.get('mobile'),
        iname=request.POST.get('iname'),
        assignment1=request.POST.get('a1'),
        assignment2=request.POST.get('a2'),
        assignment3=request.POST.get('a3'),
        ).save()
        #sdatade=sdata.objects.all().values()
        return redirect('mainpage' )


def update_data(request,id):
    student=sdata.objects.get(id=id)
    if request.method=='GET':
      return render(request,'update_data.html',{'student':student})
    else:
        student.fname=request.POST.get('fname')
        student.lname=request.POST.get('lname')
        student.email=request.POST.get('email')
        student.mobile=request.POST.get('mobile')
        student.iname=request.POST.get('iname')
        student.assignment1=request.POST.get('assignment1')
        student.assignment2=request.POST.get('assignment2')
        student.assignment3=request.POST.get('assignment3')
        student.save()
        return redirect('mainpage')

def delete_data(request,id):
    student=sdata.objects.get(id=id)
    student.delete()
    return redirect('mainpage')
