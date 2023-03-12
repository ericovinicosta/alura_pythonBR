from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self._cpf = documento
        else:
            raise ValueError('CPF Inválido')

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            False

    def _formata_cpf(self):
        cpf = CPF()
        return cpf.mask(self._cpf)

    def __str__(self):
        return self._formata_cpf()