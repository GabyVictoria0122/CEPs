# from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from cep.models import Cep


def ola_ceps(request):
    return HttpResponse('Olá Ceps')


def api_ceps(request, cep):
    # cep = get_object_or_404(Cep)
    achar = Cep.objects.get(cep=cep)
    dados = {"rua": achar.rua, "bairro": achar.bairro, "cidade": achar.cidade, "estado": achar.estado}
    return JsonResponse(dados)
