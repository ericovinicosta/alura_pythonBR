from cpf_cnpj import Documento


cpf = Documento.cria_documento(input('Digite o cpf para verificar(apenas números): '))
# cpf = Cpf('04538019396')

print(cpf)

cnpj = Documento.cria_documento(input('Digite o cnpj para verificar(apenas números): '))

print(cnpj)