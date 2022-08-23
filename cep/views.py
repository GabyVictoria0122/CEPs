# from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from cep.models import Cep


def ola_ceps(request):
    if request.method == 'POST':
        cep = request.POST['cep']
        achar = Cep.objects.get(cep=cep)
    else:
        achar = None
    return render(request, 'cep/index.html', {'achar': achar})
# def resultado(request, cep):
#     return render(request, ')


def api_ceps(request, cep):
    # cep = get_object_or_404(Cep)
    achar = Cep.objects.get(cep=cep)
    dados = {"rua": achar.rua, "bairro": achar.bairro, "cidade": achar.cidade, "estado": achar.estado, "complemento": achar.complemento}
    return JsonResponse(dados)
