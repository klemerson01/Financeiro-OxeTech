from django.db import models
from fornecedor.models.fornecedor import Base
    
class Categoria(Base):
    nome = models.CharField(max_length=50, blank=False, null=False)
    