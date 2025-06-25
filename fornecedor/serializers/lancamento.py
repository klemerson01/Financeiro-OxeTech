from rest_framework import serializers
from fornecedor.models.lancamento import Lancamento
    


class LancamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lancamento
        fields = '__all__'
        
    def validate(self, attrs):
        valor = attrs['valor']
        valor_efetivado = attrs['valor_efetivado']
        data_efetivacao = attrs['data_efetivacao']
        vencimento = attrs['vencimento']

        if valor is not None and valor < 0:
            raise serializers.ValidationError({'valor': 'Valor não pode ser negativo.'})

        if valor_efetivado is not None and valor_efetivado < 0:
            raise serializers.ValidationError({'valor_efetivado': 'Valor efetivado não pode ser negativo.'})


        if valor_efetivado and valor_efetivado < valor:
            print('faça uma copia')
        
        if data_efetivacao and vencimento and data_efetivacao > vencimento:
            raise serializers.ValidationError(
                {"data_efetivacao": "Data de efetivação não pode ser maior que a data de vencimento."}
            )

        return attrs
    
    def create(self, validated_data):
        valor = validated_data.get('valor')
        valor_efetivado = validated_data.get('valor_efetivado')

        lancamento = super().create(validated_data)

        if valor_efetivado is not None and valor_efetivado < valor:
            restante = valor - valor_efetivado
            novo_dados = validated_data.copy()
            novo_dados['valor'] = restante
            novo_dados['valor_efetivado'] = None
            novo_dados['data_efetivacao'] = None
            Lancamento.objects.create(**novo_dados)

        return lancamento
    
    
       
       
    # Repetição do lançamento, com 30 dias de diferença entre cada
    # repetição 