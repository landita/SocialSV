from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Publicaciones
from .forms import PublicarForm

# Create your views here.

@login_required(login_url='/account/login/')
def listar(request):
    context = Publicaciones.objects.filter(autor=request.user)
    return render(request, 'posts/index.html', {'queries':context})

def crear(request):
    if request.method == 'POST':
        form = PublicarForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('/posts')
    else:
        form = PublicarForm()
    return render(request, 'posts/crear.html', {'form':form})

@login_required(login_url='/account/login/')
def editar(request, id):
    instance = get_object_or_404(Publicaciones, pk=id)
    if request.method == 'POST':
        form = PublicarForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    else:
        form = PublicarForm(instance=instance)
    return render(request, 'posts/editar.html', {'form':form})

@login_required(login_url='/account/login/')
def detalles(request, id):
    context = get_object_or_404(Publicaciones, pk=id)
    return render(request, 'posts/mostrar.html', {'context':context})

@login_required(login_url='/account/login/')
def publicaciones(request):
    return render(request, 'posts/publicaciones.html')

@login_required(login_url="/account/login/")
def detallePublicacion(request, id):
    publicacion = get_object_or_404(Publicaciones, pk=id)
    return render(request, 'posts/detalle-publicacion.html', {'query':publicacion})

#ajax methods
@login_required(login_url='/account/login/')
def eliminar(request, id):
    context = get_object_or_404(Publicaciones, pk=id)
    context.delete()
    return JsonResponse({'success':True})

@login_required(login_url='/account/login/')
def listarPublicaciones(request):
    context = Publicaciones.objects.all().values(
        'id',
        'titulo',
        'categoria',
        'fechaRegistro',
        'autor__id',
        'autor__email',
    )
    return JsonResponse({'data':list(context)})

@login_required(login_url='/account/login/')
def filtrarPorFecha(request):
    context = Publicaciones.objects.all().order_by('fechaRegistro').values(
        'id',
        'titulo',
        'categoria',
        'fechaRegistro',
        'autor__id',
        'autor__email',
    )
    return JsonResponse({'data':list(context)})  

@login_required(login_url='/account/login/')
def filtrarPorBusqueda(request, query):
    context = Publicaciones.objects.filter(
        Q(titulo__startswith=query) | 
        Q(categoria__startswith=query) |
        Q(autor__email__startswith=query)
    ).values(
        'id',
        'titulo',
        'categoria',
        'fechaRegistro',
        'autor__id',
        'autor__email',   
    )
    return JsonResponse({'data':list(context)})  

