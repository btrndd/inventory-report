from inventory_report.inventory.product import Product


def test_cria_produto():
    ID = 1
    NOME_DO_PRODUTO = 'produto'
    NOME_DA_EMPRESA = 'empresa'
    DATA_DE_FAB = '10/02/2022'
    DATA_DE_VAL = '20/12/2022'
    NUMERO_DE_SERIE = 252145
    INSTRUCOES_DE_ARMAZENAMENTO = 'Local seco e longe do sol'

    product = Product(
        ID,
        NOME_DO_PRODUTO,
        NOME_DA_EMPRESA,
        DATA_DE_FAB, DATA_DE_VAL,
        NUMERO_DE_SERIE,
        INSTRUCOES_DE_ARMAZENAMENTO
    )

    assert product.id == ID
    assert product.nome_do_produto == NOME_DO_PRODUTO
    assert product.nome_da_empresa == NOME_DA_EMPRESA
    assert product.data_de_fabricacao == DATA_DE_FAB
    assert product.data_de_validade == DATA_DE_VAL
    assert product.numero_de_serie == NUMERO_DE_SERIE
    assert product.instrucoes_de_armazenamento == INSTRUCOES_DE_ARMAZENAMENTO
