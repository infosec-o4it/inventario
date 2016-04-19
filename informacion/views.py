from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm, Form, CharField
from informacion.models import activo
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.


class BuscarForm(Form):
    nombre_activo = CharField(label='Nombre del Activo', max_length=100)


class ActivosForm(ModelForm):
    class Meta:
        model = activo
        fields = ['activo', 'descripcion', 'ubicacion', 'area',  'responsable']


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def ingresa_activo(request):
    if request.method == 'POST':
        form = ActivosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/informacion/')
    else:
        form = ActivosForm()

    return render(request, 'informacion/index.html', {'form': form, })


@require_http_methods(["GET", "POST"])
@login_required(login_url='/admin/')
def busca_activo(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            consulta = form.cleaned_data['nombre_activo']
            busqueda = activo.objects.filter(activo__icontains=consulta)
            context = {'busqueda': busqueda}
            return render(request, 'informacion/buscar_activo.html', context)
    else:
        form = BuscarForm()
        context = {'form': form, }

    return render(request, 'informacion/buscar_activo.html', context)
