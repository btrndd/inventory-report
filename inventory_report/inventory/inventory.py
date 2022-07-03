import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    def read(path):
        with open(path, encoding="utf8") as file:
            report_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            json_result = [row for row in report_reader]
            return json_result

    @classmethod
    def import_data(cls, path, type):
        product_list = cls.read(path)
        if (type == 'simples'):
            return SimpleReport.generate(product_list)
        elif(type == 'completo'):
            return CompleteReport.generate(product_list)
