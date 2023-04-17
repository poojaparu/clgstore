

from django.shortcuts import render, get_object_or_404

from store.models import  Course,Department


# Create your views here.


def department(request, c_slug=None):
    c_page = None
    dept = None
    if c_slug != None:
        c_page = get_object_or_404(Course, slug=c_slug)
        dept = Department.objects.all().filter(course=c_page, available=True)
    else:
        dept = Department.objects.all().filter(available=True)
    return render(request, "course.html", {'course': c_page, 'dept': dept})

def deptdetail(request,c_slug,dept_slug):
    try:
        dept=Department.objects.get(course__slug=c_slug,slug=dept_slug)
    except Exception as e:
        raise e
    return render(request,'department.html',{'dept':dept})








