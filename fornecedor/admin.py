from django.contrib import admin
from fornecedor.models import (
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

admin.site.register(Estado,EstadoAdmin)
admin.site.register(Cidade,CidadeAdmin)