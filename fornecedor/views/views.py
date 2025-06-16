from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from fornecedor.models.fornecedor import (
    Fornecedor,
    Cidade,
    Estado
)
from fornecedor.serializers.serializers import (
    FornecedorSerializer,
    CidadeSerializer,
    EstadoSerializer
)
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from fornecedor.tasks import add


class FornecedorViewSet(APIView):

    def get_object(self, pk):
        try:
            return Fornecedor.objects.get(pk=pk)
        except Fornecedor.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        add.delay(10, 10)
        if pk:
            fornecedor = Fornecedor.objects.get(id=pk)
            serializer = FornecedorSerializer(fornecedor)
            return JsonResponse(serializer.data, safe=False)

        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = FornecedorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        fornecedor = self.get_object(pk)
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(pk)
        fornecedor = self.get_object(pk)
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EstadoViewSet(APIView):

    def get_object(self, pk):
        try:
            return Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            estado = Estado.objects.get(id=pk)
            serializer = EstadoSerializer(estado)
            return JsonResponse(serializer.data, safe=False)

        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = EstadoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        estado = self.get_object(pk)
        serializer = EstadoSerializer(estado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(pk)
        estado = self.get_object(pk)
        estado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CidadeViewSet(APIView):

    def get_object(self, pk):
        try:
            return Cidade.objects.get(pk=pk)
        except Cidade.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            cidade = Cidade.objects.get(id=pk)
            serializer = CidadeSerializer(cidade)
            return JsonResponse(serializer.data, safe=False)

        cidades = Cidade.objects.all()
        serializer = CidadeSerializer(cidades, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = CidadeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        cidade = self.get_object(pk)
        serializer = CidadeSerializer(cidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(pk)
        cidade = self.get_object(pk)
        cidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
