from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

# Create your views here.
from cep.models import Cep


def ola_ceps(request):
    return HttpResponse('Olá Ceps')


def api_ceps(request):
    # cep = get_object_or_404(Cep)
    achar = Cep.objects.all()
    claytinho = print('Pra entrar tem que pedir autorização pro caciqui')
    return JsonResponse(achar[0], claytinho)
