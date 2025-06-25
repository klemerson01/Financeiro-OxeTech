from django.http import JsonResponse
from fornecedor.models.categoria import Categoria
from fornecedor.serializers.categoria import CategorialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CategoriaViewSet(APIView):
    
    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None):
        if pk:
            categoria = Categoria.objects.get(id=pk)
            
            serializer = CategorialSerializer(categoria)
            return JsonResponse(serializer.data, safe=False)

        categorias = Categoria.objects.all()
        serializer = CategorialSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)
    

    def post(self, request):
        serializer = CategorialSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, pk):
        categoria = self.get_object(pk)
        serializer = CategorialSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
