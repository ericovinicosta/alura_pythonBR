from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Documento inválido')

class DocCpf:
    def __init__(self, documento):
        if self._valida(documento):
            self._cpf = documento
        else:
            raise ValueError('CPF Inválido!!')

    def _valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def _formata(self):
            cpf = CPF()
            return cpf.mask(self._cpf)

    def __str__(self):
        return self._formata()

class DocCnpj:
    def __init__(self, documento):
        if self._valida(documento):
            self._cnpj = documento
        else:
            raise ValueError('CNPJ Inválido!!')

    def _valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def _formata(self):
            cnpj = CNPJ()
            return cnpj.mask(self._cnpj)

    def __str__(self):
        return self._formata()