
from pydantic import BaseModel

class GetConsultaGeralSeniorDTO(BaseModel):
    codigo_empresa: str
    codigo_filial: str
    data_inicio: str | None = None
    data_fim: str | None = None