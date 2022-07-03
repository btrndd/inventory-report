from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_company_products_qty(product_list):
        companies_name_list = map(
            lambda product: product["nome_da_empresa"],
            product_list
        )
        company_stock_dict = Counter(companies_name_list).items()
        return Counter(company_stock_dict)

    @classmethod
    def generate(cls, product_list):
        company_stock_dict = cls.get_company_products_qty(product_list)

        company_name_and_stock_qty = ""

        for company in company_stock_dict:
            company_name_and_stock_qty += f'- {company[0]}: {company[1]}\n'

        return (
          f'{super().generate(product_list)}\n'
          'Produtos estocados por empresa:\n'
          f'{company_name_and_stock_qty}'
        )
