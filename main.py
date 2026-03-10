import asyncio

from app.database.config import init
from app.use_cases.consulta_use_case import ConsultarGeralUseCase


async def main():
    await init()
    request = {
        "codigo_empresa": "10",
        "codigo_filial": "1001"
    }
    use_case = ConsultarGeralUseCase(request)
    result = await use_case.execute()
    print(result)

asyncio.run(main())