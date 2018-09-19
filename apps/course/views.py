from django.shortcuts import render, redirect
from apps.course.models import Course
from apps.course.form import CourseForm
from django.db.models import Q
from sweetify import *
# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'object_list': courses})


def create(request):
    if request.method == 'POST':
        CourseForm(request.POST).save()
        success(request, 'Curso guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('course:index')
    return render(request, 'course/create.html', {'form': CourseForm})


def edit(request, id_course):
    course = Course.objects.get(pk=id_course)
    if request.method == 'POST':
        CourseForm(request.POST, instance=course).save()
        success(request, 'Editado correctamente!', toast=True, position='top', timer=2000)
        return redirect('course:index')
    return render(request, 'course/edit.html', {'form': CourseForm(instance=course)})


def show(request):
    pass


def delete(request, id_course):
    Course.objects.get(pk=id_course).delete()
    return render(request, 'course/table.html')


def enroll(request, id_ins):
    courses = Course.user.add()
    pass


def table(request):
    courses = Course.objects.all()
    return render(request, 'course/table.html', {'object_list': courses})


def search(request, find):
    courses = Course.objects.filter(
        Q(name__icontains=find) |
        Q(language__course__name__contains=find)
    )
    return render(request, 'course/table.html', {'object_list': courses})
