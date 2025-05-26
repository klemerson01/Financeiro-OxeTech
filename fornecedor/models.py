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
    