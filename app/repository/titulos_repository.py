from app.database.models import TitulosContasPagar, RateioTituloContasPagar


class TitulosRepository:

    async def create_titulo(self, data: dict) -> TitulosContasPagar:
        return await TitulosContasPagar.create(**data)

    async def create_many_rateio(self, rateios: list[dict]):

        objs = [RateioTituloContasPagar(**r) for r in rateios]

        await RateioTituloContasPagar.bulk_create(objs)

    async def titulo_exists(
        self,
        codigo_empresa: int,
        codigo_filial: int,
        numero_titulo: str
    ) -> bool:

        return await TitulosContasPagar.filter(
            codigo_empresa=codigo_empresa,
            codigo_filial=codigo_filial,
            numero_titulo=numero_titulo
        ).exists()