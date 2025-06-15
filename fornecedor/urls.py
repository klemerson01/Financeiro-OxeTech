from django.urls import path
from fornecedor.views.views import FornecedorViewSet
from fornecedor.views.views import CidadeViewSet
from fornecedor.views.views import EstadoViewSet

urlpatterns = [
    path('fornecedores', view=FornecedorViewSet.as_view()),
    path('fornecedores/<int:pk>', view=FornecedorViewSet.as_view()),
    path('cidades', view=CidadeViewSet.as_view()),
    path('cidades/<int:pk>', view=CidadeViewSet.as_view()),
    path('estados', view=EstadoViewSet.as_view()),
    path('estados/<int:pk>', view=EstadoViewSet.as_view()),
]