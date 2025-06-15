from django.contrib import admin
from fornecedor.models.fornecedor import (
    Estado, 
    Cidade,
    Fornecedor
)

class EstadoAdmin(admin.ModelAdmin):

    class Meta:
        model = Estado

class CidadeAdmin(admin.ModelAdmin):

    class Meta:
        model = Cidade

class FornecedorAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Fornecedor

admin.site.register(Estado,EstadoAdmin)
admin.site.register(Cidade,CidadeAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)