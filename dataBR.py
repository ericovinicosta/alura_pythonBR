from datetime import datetime, timedelta

class DataBr:
    _meses_ano = [
        'janeiro','fevereiro','março',
        'abril', 'maio', 'junho', 'julho',
        'agosto','setembro','outubro',
        'novembro','dezembro'
    ]

    def mes_cadastro(self):
        mes_cadastro = self.data_cadastro.month - 1
        return self._meses_ano[mes_cadastro]

    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self) -> str:
        data = f'{self.dia_da_semana()} - {self.formata_data()}'
        return data

    def formata_data(self):
        return self.data_cadastro.strftime("%d/%m/%Y %H:%M")

    def dia_da_semana(self):
        dia_da_semana = [
            'segunda','terça','quarta','quinta','sexta','sábado','domingo',
        ]
        semana = self.data_cadastro.weekday()
        return dia_da_semana[semana]