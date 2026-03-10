from tortoise.models import Model
from tortoise import fields


class TitulosContasPagar(Model):
    id = fields.IntField(pk=True)
    codigo_empresa = fields.IntField(description="codEmp")
    codigo_filial = fields.IntField(description="codFil")
    codigo_fornecedor = fields.IntField(description="codFor")
    codigo_transacao = fields.IntField(description="codTns")
    codigo_tipo_titulo = fields.IntField(description="codTpt")
    data_emissao = fields.DateField(description="datEmi")
    data_entrada = fields.DateField(description="datEnt")
    data_provavel_pgt = fields.DateField(null=True, description="datPgt")
    situacao_titulo = fields.CharField(max_length=255, description="staTit")
    descricao_situacao = fields.CharField(max_length=255, description="desSit")
    descricao_transacao = fields.CharField(max_length=255, description="desTns")
    descricao_tipo_titulo = fields.CharField(max_length=255, description="desTpt")
    filial_nota_fiscal = fields.IntField(null=True, description="filNfc")
    fornecedor_nota_fiscal = fields.IntField(null=True, description="forNfc")
    nome_fornecedor = fields.CharField(max_length=255, description="nomFor")
    numero_nota_fiscal = fields.IntField(null=True, description="numNfc")
    numero_titulo = fields.CharField(max_length=255, description="numTit")
    observacao_titulo = fields.TextField(null=True, description="obsTit")
    valor_titulo = fields.IntField(description="valTit")
    serie_nota_fiscal = fields.CharField(max_length=255, null=True, description="snfNfc")
    vencimento_original = fields.DateField(description="vctOri")
    vencimento_prorrogado = fields.DateField(null=True, description="vctPro")
    valor_aberto = fields.IntField(description="valAbr")
    valor_original = fields.IntField(description="vlrOri")

    class Meta:
        table = "task_api_titulos_contas_pagar"
        unique_together = ("codigo_empresa", "codigo_filial", "numero_titulo")


class RateioTituloContasPagar(Model):
    id = fields.IntField(pk=True)
    codigo_empresa = fields.IntField(description="codEmp")
    codigo_filial = fields.IntField(description="codFil")
    codigo_centro_custo = fields.IntField(description="codCcu")
    descricao_centro_custo = fields.CharField(max_length=255, description="desCcu")
    codigo_fase = fields.IntField(description="codFpj")
    numero_projeto = fields.IntField(description="numPrj")
    codigo_conta_financeira = fields.IntField(description="ctaFin")
    descricao_conta_financeira = fields.CharField(max_length=255, description="desFin")
    conta_contabil = fields.IntField(description="ctaRed")
    descricao_conta_contabil = fields.CharField(max_length=255, description="desRed")
    data_base_contabil = fields.DateField(description="datBas")
    percentual_rateio = fields.IntField(description="perCta")
    sequencia_rateio = fields.IntField(description="seqRat")
    valor_rateio = fields.IntField(description="vlrCta")
    percentual_rateio_centro_custo = fields.IntField(description="perRat")
    valor_rateio_centro_custo = fields.IntField(description="vlrRat")
    class Meta:
        table = "task_api_rateio_titulo_contas_pagar"
        unique_together = ("codigo_empresa", "codigo_filial", "sequencia_rateio")