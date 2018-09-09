from django.shortcuts import render, redirect
from apps.user.models import User
from apps.user.form import UserForm
from passlib.hash import pbkdf2_sha256
import sweetify
from sweetify.views import SweetifySuccessMixin


def index(request):
    user = User.objects.all()
    return render(request, 'user/index.html', {'object_list': user})


def create(request):
    if request.method == 'POST':
        User.objects.create(
            code=request.POST['code'],
            password=pbkdf2_sha256.encrypt(request.POST['password'], rounds=12000, salt_size=32),
            nombre=request.POST['nombre'],
            apaterno=request.POST['apaterno'],
            amaterno=request.POST['amaterno'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            role_id=request.POST['role'],
        )
        sweetify.success(request, 'Usuario guardado correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')
    return render(request, 'user/create.html', {'form': UserForm})


def edit(request):
    if request.method == 'POST':
        # content
        sweetify.success(request, 'Cambios aplicados correctamente!', toast=True, position='top', timer=2000)
        return redirect('user:index')
    return render(request, 'user/edit.html', {'form': UserForm})


def show(request, code):
    user = User.objects.get(pk=code)
    return render(request, 'user/show.html', {'object_list': user})


def delete(request, code):
    User.objects.get(pk=code).delete()
    return render(request, 'user/table.html')


def table(request):
    user = User.objects.all()
    return render(request, 'user/table.html', {'object_list': user})


def search(request):
    user = User.objects. \
        get(code__contains=request['search'],
            nombre__contains=request['search'],
            apaterno__contains=request['search'],
            amaterno__contains=request['search'],
            )
    return render(request, 'user/table.html', {'object_list': user})
