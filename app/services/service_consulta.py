import logging
import os
from dotenv import load_dotenv
from zeep.exceptions import TransportError
from requests.exceptions import ConnectTimeout
from urllib3.exceptions import MaxRetryError
from app.helpers.base_zeep import BaseSoapSenior

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class GetConsultaGeralService:
    def __init__(self):
        self.base_soap_senior = BaseSoapSenior

    def get_nota_fiscal_entrada(self, dto) -> dict:
        wsdl_url = "g5-senior-services/sapiens_Synctotallife_custom_contasapagar?wsdl"
        client = self.base_soap_senior.create_client_base(wsdl_url)
        usuario = os.getenv("USER_SENIOR")
        senha = os.getenv("PASSWORD_SENIOR")

        try:
            response = client.service.ConsultaCompletaTituloAPagar(
                user=usuario,
                password=senha,
                encryption=0,
                parameters=dto,
            )
            return response
        except (ConnectTimeout, MaxRetryError, TransportError) as specific_error:
            logging.error(f"Erro na conexão com o webservice: {specific_error}")
            return {"retorno": "Erro ao conectar com o webservice.", "situacao": "erro", "message": str(specific_error)}
        except Exception as e:
            logging.error(f"Erro inesperado: {e}", exc_info=True)
            return {"retorno": "Ocorreu um erro inesperado.", "situacao": "erro", "message": str(e)}
