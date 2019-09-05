from django.shortcuts import render, get_object_or_404
from django.utils  import timezone
from .models import Publicacion

def listar_pub(request):
    pubs = Publicacion.objetcs.filter(fecha_publicacion_lte=timezone.now()).order.by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html',{'pubs': pubs})

def detalle_pub(request,pk):
    p = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html',{'p':p})
