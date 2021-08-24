from django.shortcuts import render
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=user)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)