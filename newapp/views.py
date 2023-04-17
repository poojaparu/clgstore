from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from newapp.forms import StudentForm
from newapp.models import Purpose,Form, Department,Course

from django.shortcuts import render

# Create your views here.

def department(request):
    courseid=request.GET.get('course',None)
    departmentid = request.GET.get('department', None)
    department=None
    if courseid:
        getcourse=Course.objects.get(id=courseid)
        department=Department.objects.filter(course=getcourse)
    if departmentid:
        getdepartment = Course.objects.get(id=departmentid)
        course=Course.objects.all()

    return render(request,'form.html',locals())


def CreateView(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "order confirmed")
            return redirect('newapp:add')
    return render(request,'form.html',{'form':form})

def UpdateView(request,pk):
    student = get_object_or_404(Form, pk=pk)
    form=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "order confirmed")
            return redirect('newapp:change')
    return render(request,'form.html',{'form':form})