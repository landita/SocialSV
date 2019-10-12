from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import UsuarioForm


# Create your views here.
@login_required(login_url='/account/login/')
def perfilAutor(request, id):
    context = get_object_or_404(User, pk=id)
    return render(request, 'account/perfil-autor.html', {'autor':context})

@login_required(login_url='/account/login/')
def perfilEditar(request, id):
    instance = get_object_or_404(User, pk=id)
    if instance != request.user:
        return redirect('/posts')
    else:
        if request.method == 'POST':
            form = UsuarioForm(request.POST or None,instance=instance)
            if form.is_valid:
                form.save()
                return redirect('/posts')
        else:
            form = UsuarioForm(instance=instance)
    return render(request, 'account/perfil-editar.html', {'autor':form})

@login_required(login_url='/account/login')
def usuarios(request):
    if not request.user.is_superuser:
        redirect('/posts')
    context = User.objects.filter(is_superuser=False)
    return render(request, 'account/usuarios.html', {'query':context})

@login_required(login_url='/account/login')
def desactivarUsuarios(request, id):
    context = get_object_or_404(User, pk=id)
    context.is_activate = False
    context.save()
    return JsonResponse({'success':True})



