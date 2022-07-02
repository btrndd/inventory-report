from inventory_report.inventory.product import Product


def test_relatorio_produto():
    ID = 1
    NOME_DO_PRODUTO = 'produto'
    NOME_DA_EMPRESA = 'empresa'
    DATA_DE_FAB = '10/02/2022'
    DATA_DE_VAL = '20/12/2022'
    NUMERO_DE_SERIE = 252145
    INSTRUCOES_DE_ARMAZENAMENTO = 'seco e longe de luz do sol'

    product = Product(
        ID,
        NOME_DO_PRODUTO,
        NOME_DA_EMPRESA,
        DATA_DE_FAB, DATA_DE_VAL,
        NUMERO_DE_SERIE,
        INSTRUCOES_DE_ARMAZENAMENTO
    )

    product_report = (
        f"O produto {NOME_DO_PRODUTO}"
        f" fabricado em {DATA_DE_FAB}"
        f" por {NOME_DA_EMPRESA} com validade"
        f" até {DATA_DE_VAL}"
        f" precisa ser armazenado {INSTRUCOES_DE_ARMAZENAMENTO}."
    )

    repr = str(product.__repr__())

    assert repr == product_report
