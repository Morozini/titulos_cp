from datetime import datetime
from zeep.helpers import serialize_object

from app.dto.get_consultar_dto import GetConsultaGeralSeniorDTO
from app.helpers.base_zeep import BaseSoapSenior
from app.mappers.create_consulta_mapper import CreateConsultaGeralMapper
from app.services.service_consulta import GetConsultaGeralService
from app.repository.titulos_repository import TitulosRepository


class ConsultarGeralUseCase:

    def __init__(self, request):

        self.base_soap_senior = BaseSoapSenior
        wsdl_url = "g5-senior-services/sapiens_Synctotallife_custom_contasapagar?wsdl"
        self.client = self.base_soap_senior.create_client_base(wsdl_url)
        self.dto = GetConsultaGeralSeniorDTO(**request)
        self.mapper = CreateConsultaGeralMapper(self.client)
        self.payload_mapper = self.mapper.payload(self.dto)
        self.service = GetConsultaGeralService()
        self.repository = TitulosRepository()

    async def execute(self):

        response = self.service.get_nota_fiscal_entrada(self.payload_mapper)

        response = serialize_object(response)

        print("RESPONSE:", response)

        titulos = response.get("titulos", [])

        # garantir lista
        if isinstance(titulos, dict):
            titulos = [titulos]

        print("TOTAL TITULOS ENCONTRADOS:", len(titulos))

        for titulo in titulos:

            titulo_mapper = self.mapper.map_titulo(titulo)

            exists = await self.repository.titulo_exists(
                titulo_mapper["codigo_empresa"],
                titulo_mapper["codigo_filial"],
                titulo_mapper["numero_titulo"]
            )

            if not exists:
                await self.repository.create_titulo(titulo_mapper)

            movimentos = titulo.get("movimentos") or []

            if isinstance(movimentos, dict):
                movimentos = [movimentos]

            rateios_mapper = []

            for movimento in movimentos:

                rateios = movimento.get("rateios") or []

                if isinstance(rateios, dict):
                    rateios = [rateios]

                for rateio in rateios:

                    mapped = self.mapper.map_rateio(
                        titulo,
                        movimento,
                        rateio
                    )

                    rateios_mapper.append(mapped)

            if rateios_mapper:
                await self.repository.create_many_rateio(rateios_mapper)

        return {
            "message": "Consulta realizada com sucesso",
            "quantidade_titulos": len(titulos),
            "data_execucao": datetime.now()
        }