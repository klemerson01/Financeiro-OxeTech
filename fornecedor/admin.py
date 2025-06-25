from django.contrib import admin
from fornecedor.models.fornecedor import (
    Estado, 
    Cidade,
    Fornecedor
)
from fornecedor.models.forma_pagamento import FormaPagamento
   
from fornecedor.models.categoria import  Categoria


class EstadoAdmin(admin.ModelAdmin):

    class Meta:
        model = Estado

class CidadeAdmin(admin.ModelAdmin):

    class Meta:
        model = Cidade

class FornecedorAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Fornecedor

class FormaPagamentoAdmin(admin.ModelAdmin):
    
    class Meta:
        model = FormaPagamento
        
        
class CategoriaAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Categoria


admin.site.register(Estado,EstadoAdmin)
admin.site.register(Cidade,CidadeAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(FormaPagamento, FormaPagamentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)