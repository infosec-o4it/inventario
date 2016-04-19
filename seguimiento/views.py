from django.http import HttpResponse
from django.db.models import Sum, Count
from seguimiento.tools import percen
from django.shortcuts import render
from seguimiento.models import seccion, hallazgo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/admin/')
def index(request):
    latest_seccion_list = hallazgo.objects.values(
        'punto__numeral__control__seccion',
        'punto__numeral__control__seccion__descripcion'
        ).annotate(
        total=Sum('nota'), cantidad=Count('punto')).order_by('-punto')
    numeros_hallazgos = hallazgo.objects.values(
        'punto__numeral', 'punto__numeral__descripcion').annotate(
        total=Sum('nota'), cantidad=Count('punto'), numerales=Count('punto')
        ).order_by('-punto')
    porcentajes_seccion_list = \
        percen(latest_seccion_list,
               "punto__numeral__control__seccion__descripcion")
    porcentajes_numeral = \
        percen(numeros_hallazgos, "punto__numeral__descripcion")
    context = {
        'latest_seccion_list': latest_seccion_list,
        'numeros_hallazgos': numeros_hallazgos,
        'porcentajes_numeral': porcentajes_numeral,
        'porcentajes_seccion_list': porcentajes_seccion_list,
    }
    return render(request, 'seguimiento/index.html', context)
