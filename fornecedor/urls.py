from django.urls import path
from fornecedor.views.fornecedor import (
    FornecedorViewSet,
    CidadeViewSet,
    EstadoViewSet
    )
from fornecedor.views.lancamento import LancamentoViewSet
from fornecedor.views.forma_pagamento import FormaPagamentoViewSet
from fornecedor.views.categoria import CategoriaViewSet
from fornecedor.views.repetir_lancamento import RepetirLancamentoViewSet

urlpatterns = [
    path('fornecedores', view=FornecedorViewSet.as_view()),
    path('fornecedores/<int:pk>', view=FornecedorViewSet.as_view()),
    path('cidades', view=CidadeViewSet.as_view()),
    path('cidades/<int:pk>', view=CidadeViewSet.as_view()),
    path('estados', view=EstadoViewSet.as_view()),
    path('estados/<int:pk>', view=EstadoViewSet.as_view()),
    path('lancamentos', view=LancamentoViewSet.as_view()),
    path('lancamentos/<int:pk>', view=LancamentoViewSet.as_view()),
    path('lancamentos/<int:pk>/repetir/', RepetirLancamentoViewSet.as_view()),
    path('formapagamentos', view=FormaPagamentoViewSet.as_view()),
    path('formapagamentos/<int:pk>', view=FormaPagamentoViewSet.as_view()),
    path('categorias', view=CategoriaViewSet.as_view()),
    path('categorias/<int:pk>', view=CategoriaViewSet.as_view()),
]