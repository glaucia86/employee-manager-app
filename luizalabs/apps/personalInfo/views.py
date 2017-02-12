from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_personal(request):
    return HttpResponse("Página - Dados dos Funcionários")