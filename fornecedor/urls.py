from django.urls import path
from fornecedor import views

urlpatterns = [
    path('fornecedor/', views.fornecedor_list),
    
]