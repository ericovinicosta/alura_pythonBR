import re

class TelefoneBR:
    def __init__(self, telefone):
        if self.valida(telefone):
            self._telefone = telefone
        else:
            raise ValueError("Número não é válido!!!")

    def valida(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        ocorencia = re.findall(padrao, telefone)
        if ocorencia:
            return True
        else:
            return False

    def __str__(self):
        self.formata()
    
    def formata(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        ocorrencia = re.search(padrao, self._telefone)
        numero = '+{} ({}) {}-{}'.format(
            ocorrencia.group(1),
            ocorrencia.group(2),
            ocorrencia.group(3),
            ocorrencia.group(4)
        )
        return numero
