import json
from zeep.helpers import serialize_object

from app.use_cases.consulta_use_case import ConsultarGeralUseCase


request = {
    "codigo_empresa": "10",
    "codigo_filial": "1001"
}

use_case = ConsultarGeralUseCase(request)
response = use_case.execute()
data = serialize_object(response)

with open("retorno.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)