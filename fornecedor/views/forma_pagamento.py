from django.http import JsonResponse
from fornecedor.models.forma_pagamento import FormaPagamento
from fornecedor.serializers.forma_pagamento import FormaPagamentoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class FormaPagamentoViewSet(APIView):
    
    def get_object(self, pk):
        try:
            return FormaPagamento.objects.get(pk=pk)
        except FormaPagamento.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None):
        if pk:
            formapagamento = FormaPagamento.objects.get(id=pk)
            
            serializer = FormaPagamentoSerializer(formapagamento)
            return JsonResponse(serializer.data, safe=False)

        formapagamentos = FormaPagamento.objects.all()
        serializer = FormaPagamentoSerializer(formapagamentos, many=True)
        return JsonResponse(serializer.data, safe=False)
    

    def post(self, request):
        serializer = FormaPagamentoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = FormaPagamentoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        formapagamento = self.get_object(pk)
        formapagamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
