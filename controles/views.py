from django.http import HttpResponse
from controles.models import Control

from django.shortcuts import render


def index(request):
    latest_control_list = Control.objects.all().order_by('-dominio')
    context = {'latest_control_list': latest_control_list}
    return render(request, 'controles/index.html', context)
# Create your views here.


def detail(request, control_id):
    return HttpResponse("Estas viendo el control %s." % control_id)


def results(request, poll_id):
    return HttpResponse("Estas viendo los resultados del control %s."
    % control_id)


def vote(request, poll_id):
    return HttpResponse("Estas viendo informacion del control %s."
    % control_id)