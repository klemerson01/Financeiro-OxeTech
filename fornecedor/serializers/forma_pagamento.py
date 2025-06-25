from rest_framework import serializers
from fornecedor.models.forma_pagamento import FormaPagamento


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'
    