from cpf_cnpj import Documento
from telefoneBR import TelefoneBR
from dataBR import DataBr

import cep

# cpf = Documento.cria_documento(input('Digite o cpf para verificar(apenas números): '))
# # cpf = Cpf('04538019396')

# print(cpf)

# cnpj = Documento.cria_documento(input('Digite o cnpj para verificar(apenas números): '))

# print(cnpj)

# telefone = "86988068448"

# telefone_objeto = TelefoneBR(telefone)

# print(telefone_objeto)

objeto = cep.BuscaEndereco(64218260)
cidade, uf, bairro = objeto.acessa_viacep()
print(cidade, uf, bairro, sep='\n')