import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        path_format = path[-4:]
        if (path_format == 'json'):
            with open(path) as file:
                report_reader = file.read()
                dict_result = json.loads(report_reader)
                return dict_result
        else:
            raise ValueError("Arquivo inválido")
