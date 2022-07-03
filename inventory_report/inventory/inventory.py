import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    def read(path):
        path_format = path[-4:]
        if (path_format == '.csv'):
            with open(path, encoding="utf8") as file:
                report_reader = csv.DictReader(
                  file, delimiter=",", quotechar='"'
                  )
                dict_result = [row for row in report_reader]
                return dict_result
        elif (path_format == 'json'):
            with open(path) as file:
                report_reader = file.read()
                dict_result = json.loads(report_reader)
                return dict_result
        elif (path_format == '.xml'):
            with open(path) as file:
                report_reader = file.read()
                dict_result = xmltodict.parse(report_reader)
                return dict_result["dataset"]["record"]

    @classmethod
    def import_data(cls, path, type):
        product_list = cls.read(path)
        if (type == 'simples'):
            return SimpleReport.generate(product_list)
        elif(type == 'completo'):
            return CompleteReport.generate(product_list)
