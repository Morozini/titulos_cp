from datetime import datetime
from app.dto.get_consultar_dto import GetConsultaGeralSeniorDTO


class CreateConsultaGeralMapper:

    def __init__(self, client):
        self.client = client

    def payload(self, dto: GetConsultaGeralSeniorDTO):

        param_type = self.client.get_type(
            "ns0:contasapagarConsultaCompletaTituloAPagarIn"
        )

        data_inicio = dto.data_inicio or "01/03/2026"
        data_fim = dto.data_fim or datetime.now().strftime("%d/%m/%Y")

        return param_type(
            flowInstanceID="",
            flowName="",
            codEmp=int(dto.codigo_empresa),
            codFil=int(dto.codigo_filial),
            emiIni=data_inicio,
            emiFim=data_fim
        )