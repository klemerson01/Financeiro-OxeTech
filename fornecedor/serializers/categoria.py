from rest_framework import serializers
from fornecedor.models.categoria import Categoria


class CategorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    