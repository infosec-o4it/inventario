from django.http import HttpResponse
from django.db.models import Count
from controles.models import Control, Madurez
from controles.tools import percen
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/')
def index(request):
    latest_control_list = Control.objects.all().order_by('-dominio')
    numeros_madurez = Madurez.objects.all().annotate(
        total=Count('grado')).order_by('-grado')
    porcentajes_madurez = percen(numeros_madurez)
    context = {
        'latest_control_list': latest_control_list,
        'numeros_madurez': numeros_madurez,
        'porcentajes_madurez': porcentajes_madurez
    }
    return render(request, 'controles/index.html', context)
# Create your views here.


def detail(request, control_id):
    return HttpResponse("Estas viendo el control %s." % control_id)


def results(request, poll_id):
    return HttpResponse(
        "Estas viendo los resultados del control %s." % control_id
    )


def vote(request, poll_id):
    return HttpResponse(
        "Estas viendo informacion del control %s." % control_id
    )
