from rest_framework import serializers
from fornecedor.models import fornecedor
import requests


class FornecedorSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = fornecedor.Fornecedor
        fields = '__all__'
        extra_kwargs = {
            'logradouro': {'required': False},
            'bairro': {'required': False},
            'numero': {'required': False},
        }
        #Retira a  obrigatoriedade na entrada

    def create(self, validated_data):
        cnpj = validated_data.get('cnpj')
        response = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
        dados = response.json()

        # Atualiza os dados com base na resposta da API
        validated_data.update({
            'logradouro': dados.get('logradouro'),
            'bairro': dados.get('bairro'),
            'numero': dados.get('numero'),
        })

        return super().create(validated_data)

class CidadeSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = fornecedor.Cidade
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = fornecedor.Estado
        fields = '__all__'