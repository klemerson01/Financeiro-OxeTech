from django.core.management.base import BaseCommand
from fornecedor.models.fornecedor import Fornecedor, Cidade, Estado
import xlrd
from fornecedor.tasks import enviar_email


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    

    UF_NOMES = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }


    def add_arguments(self, parser):
        print('Arguamentos')
        
    def handle(self, *args, **options):
        fornecedores_a_criar = []
        # Abrir o arquivo da planilha
        workbook = xlrd.open_workbook('teste.xls')
        # Acessar a primeira planilha
        worksheet = workbook.sheet_by_index(0)

        # Ler os valores das células
        for row in range(1, worksheet.nrows):
            cnpj = worksheet.cell_value(row, 0)
            razao = worksheet.cell_value(row, 1)
            fantasia = worksheet.cell_value(row, 2)
            telefone = worksheet.cell_value(row, 3)
            email = worksheet.cell_value(row, 4)
            uf = worksheet.cell_value(row, 5)
            estado = self.UF_NOMES.get(uf, 'Desconhecido')
            cidade = worksheet.cell_value(row, 6)
            logradouro = worksheet.cell_value(row, 7)
            bairro = worksheet.cell_value(row, 8)
            numero = worksheet.cell_value(row, 9)
            print(f"CNPJ: {cnpj} | Razao: {razao} | UF: {uf} | Estado: {estado}")

            estado, _ = Estado.objects.get_or_create(
                uf={uf},
                nome={estado}
                # Example, adjust as needed
                
            )
            
            cidade, _ = Cidade.objects.get_or_create(
                nome={cidade},  # Example, adjust as needed
                estado=estado
            )
            
            if not Fornecedor.objects.filter(cnpj=cnpj).exists():
                fornecedor = Fornecedor(
                    cnpj=cnpj,
                    razao=razao,
                    fantasia=fantasia,
                    telefone=telefone,
                    email=email,
                    cidade=cidade,
                    estado=estado,
                    logradouro=logradouro,
                    bairro=bairro,
                    numero=numero
                )
            
                fornecedores_a_criar.append(fornecedor)
            
        if fornecedores_a_criar:
            Fornecedor.objects.bulk_create(fornecedores_a_criar)
            print("Fornecedores cadastrados")
            enviar_email.delay(
            'Fornecedores Cadastrados',
            'Olá! Seu cadastro foi um sucesso.',
            'spcomputek@gmail.com'
            )
        else:
            print("Fornecedores ja existentes!")
            enviar_email.delay(
            'Fornecedores ja existentes',
            'Olá! Seu cadastro não foi concluido,pois ja existia!',
            'spcomputek@gmail.com'
            )

       