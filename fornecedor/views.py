from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from fornecedor.models import (
    Fornecedor,
    Cidade,
    Estado 
    )
from fornecedor.serializers import (
    FornecedorSerializer,
    CidadeSerializer,
    EstadoSerializer
    )

#CRIAR OU LISTAR FORNECEDOR
@csrf_exempt
def fornecedor_list(request):
   
    if request.method == 'GET':
        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FornecedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#CRIAR OU LISTAR ESTADO
@csrf_exempt
def estado_list(request):
   
    if request.method == 'GET':
        estado = Estado.objects.all()
        serializer = EstadoSerializer(estado, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EstadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#CRIAR OU LISTAR CIDADE
@csrf_exempt
def cidade_list(request):
   
    if request.method == 'GET':
        cidade = Cidade.objects.all()
        serializer = CidadeSerializer(cidade, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CidadeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#LISTAR OU DELETAR FORNECEDOR ESPECIFICO
@csrf_exempt
def fornecedor_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        fornecedor = Fornecedor.objects.get(pk=pk)
    except Fornecedor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        fornecedor = FornecedorSerializer(fornecedor)
        return JsonResponse(fornecedor.data)

    elif request.method == 'DELETE':
        fornecedor.delete()
        return HttpResponse(status=204)

#LISTAR OU DELETAR CIDADE ESPECIFICA
@csrf_exempt
def cidade_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        cidade = Cidade.objects.get(pk=pk)
    except Cidade.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        cidade = CidadeSerializer(cidade)
        return JsonResponse(cidade.data)

    elif request.method == 'DELETE':
        cidade.delete()
        return HttpResponse(status=204)

#LISTAR OU DELETAR ESTADO ESPECIFICO
@csrf_exempt
def estado_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        estado = Estado.objects.get(pk=pk)
    except Estado.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        estado = EstadoSerializer(estado)
        return JsonResponse(estado.data)

    elif request.method == 'DELETE':
        estado.delete()
        return HttpResponse(status=204)