import requests

class BuscaEndereco:

    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.cep_e_valido(cep):
            self._cep = cep
        else:
            raise ValueError('CEP inválido!')

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def acessa_viacep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self._cep)
        resp = requests.get(url)
        dados = resp.json
        return(
            dados['localidade'],
            dados['uf'],
            dados['bairro']
        )

    def cep_formatado(self):
        return f'{self._cep[:5]}-{self._cep[5:]}'

    def __str__(self) -> str:
        return self.cep_formatado(self._cep)