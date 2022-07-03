import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        path_format = path[-4:]
        if (path_format == '.xml'):
            with open(path) as file:
                report_reader = file.read()
                dict_result = xmltodict.parse(report_reader)
                return dict_result["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
