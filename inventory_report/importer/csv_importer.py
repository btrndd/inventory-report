import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        path_format = path[-4:]
        if (path_format == '.csv'):
            with open(path, encoding="utf8") as file:
                report_reader = csv.DictReader(
                  file, delimiter=",", quotechar='"'
                  )
                dict_result = [row for row in report_reader]
                return dict_result
        else:
            raise ValueError("Arquivo inválido")
