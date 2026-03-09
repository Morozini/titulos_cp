from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.dto.get_consultar_dto import GetConsultaGeralSeniorDTO

class CreateConsultaGeralMapper:
    def __init__(self, client):
        self.client = client

    def payload(self, dto):
        param_type = self.client.get_type(
            "ns0:contasapagarConsultaCompletaTituloAPagarIn"
        )

        return param_type(
            flowInstanceID="",
            flowName="",
            codEmp=int(dto.codigo_empresa),
            codFil=int(dto.codigo_filial),
            emiIni="09/03/2026",
            emiFim="09/03/2026"
        )