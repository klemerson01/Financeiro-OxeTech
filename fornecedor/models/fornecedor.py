from django.db import models

# Create your models here.

class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Estado(Base):
    nome = models.CharField(blank=False,null=False, max_length=50)
    uf = models.CharField(blank=False,null=False, max_length=2)

    def __str__(self):
        return self.nome

class Cidade(Base):
    nome = models.CharField(blank=False,null=False, max_length=50)
    estado = models.ForeignKey(Estado,on_delete=models.PROTECT,blank=False,null=False)
    
    def __str__(self):
        return self.nome

class Fornecedor(Base):
    razao = models.CharField(blank=False,null=False, max_length=200)
    fantasia = models.CharField(blank=False,null=False, max_length=100)
    cnpj = models.CharField(blank=False,null=False, max_length=14)
    telefone = models.CharField(blank=True,null=False, max_length=11)
    email = models.CharField(blank=True,null=False, max_length=100)
    cidade = models.ForeignKey(Cidade,on_delete=models.PROTECT,blank=False,null=False)
    estado = models.ForeignKey(Estado,on_delete=models.PROTECT,blank=False,null=False)
    logradouro = models.CharField(blank=False,null=False, max_length=100)
    bairro = models.CharField(blank=False,null=False, max_length=100)
    numero = models.CharField(blank=False,null=False, max_length=100)
    observacao = models.TextField(blank=True, null=True)
    
  
class FormaPagamento(Base):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    
class Categoria(Base):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    
class Lancamento(Base):
    ENTRADA = 'E'
    SAIDA = 'S'

    TIPO_LANCAMENTO = (
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída')
    )
    
    descricao = models.TextField(blank=False, null=False)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=1, blank=False, null=False, choices=TIPO_LANCAMENTO)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    valor_efetivado = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vencimento = models.DateField(blank=False, null=False)
    data_efetivacao = models.DateField(blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
