from collections import Counter


class SimpleReport():
    def get_oldest_fab_date(product_list):
        return min([product["data_de_fabricacao"] for product in product_list])

    def get_closest_val_date(product_list):
        return min(
            [product["data_de_validade"] for product in product_list])

    def get_company_most_products(product_list):
        companies_name_list = map(
            lambda product: product["nome_da_empresa"],
            product_list
        )
        companies_rep_dict = Counter(companies_name_list)
        return max(companies_rep_dict, key=companies_rep_dict.get)

    @classmethod
    def generate(cls, product_list):
        oldest_fab_date = cls.get_oldest_fab_date(product_list)
        closest_val_date = cls.get_closest_val_date(product_list)
        company_most_products = cls.get_company_most_products(
           product_list
        )

        return (
            f"Data de fabricação mais antiga: "
            f"{oldest_fab_date}\n"
            f"Data de validade mais próxima: "
            f"{closest_val_date}\n"
            f"Empresa com mais produtos: "
            f"{company_most_products}"
          )
