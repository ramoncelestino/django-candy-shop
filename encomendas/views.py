from django.shortcuts import render
from .forms import EncomendaForm
from .models import Encomenda

# Create your views here.
def create_encomenda(request):


    def month_name(month_number):
        return calendar.month_name[month_number]

    form = EncomendaForm()

    if request.method == "POST":
        form = EncomendaForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = EncomendaForm()

    context = {
        'form': form
    }

    return render(request, 'encomendas/create_encomenda.html', context)

def list_encomendas(request):

    mes = 0

    if 'mes' in request.GET:
        mes = request.GET['mes']         


    encomendas = Encomenda.objects.order_by('data_entrega')

    context = {
        'mes': mes,
        'encomendas': encomendas
    }
    return render(request, 'encomendas/list_encomendas.html', context)

