from datetime import datetime
from dateutil.relativedelta import relativedelta
from zeep.helpers import serialize_object
from app.dto.get_consultar_dto import GetConsultaGeralSeniorDTO
from app.helpers.base_zeep import BaseSoapSenior
from app.mappers.create_consulta_mapper import CreateConsultaGeralMapper
from app.services.service_consulta import GetConsultaGeralService


class ConsultarGeralUseCase:

    def __init__(self, request):
        self.base_soap_senior = BaseSoapSenior
        wsdl_url = "g5-senior-services/sapiens_Synctotallife_custom_contasapagar?wsdl"
        self.client = self.base_soap_senior.create_client_base(wsdl_url)
        self.dto = GetConsultaGeralSeniorDTO(**request)
        self.mapper = CreateConsultaGeralMapper(self.client)
        self.payload_mapper = self.mapper.payload(self.dto)
        self.service = GetConsultaGeralService()

    def execute(self):
        return self.service.get_nota_fiscal_entrada(self.payload_mapper)

