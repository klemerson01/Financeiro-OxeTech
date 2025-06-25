from fornecedor.models.lancamento import Lancamento
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta

class RepetirLancamentoViewSet(APIView):
    def post(self, request, pk):
        try:
            lancamento = Lancamento.objects.get(pk=pk)
            repeticoes = int(request.data.get('repeticoes', 1))

            novos = []
            for i in range(1, repeticoes + 1):
                novo_vencimento = lancamento.vencimento + timedelta(days=30 * i)
                novo = Lancamento.objects.create(
                    descricao=lancamento.descricao,
                    forma_pagamento=lancamento.forma_pagamento,
                    tipo=lancamento.tipo,
                    categoria=lancamento.categoria,
                    valor=lancamento.valor,
                    fornecedor=lancamento.fornecedor,
                    vencimento=novo_vencimento,
                )
                novos.append(novo.id)

            return Response({'repeticoes_criadas': novos}, status=status.HTTP_201_CREATED)

        except Lancamento.DoesNotExist:
            return Response({'erro': 'Lançamento não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'erro': str(e)}, status=status.HTTP_400_BAD_REQUEST)
