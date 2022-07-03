import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Verifique os argumentos\n")
        return

    args = sys.argv
    file_path = args[1]
    file_format = file_path[-4:]
    report_type = args[2]

    if (file_format == '.csv'):
        inventory = InventoryRefactor(CsvImporter)
        report = inventory.import_data(file_path, report_type)
        sys.stdout.write(report)
        return
    elif(file_format == 'json'):
        inventory = InventoryRefactor(JsonImporter)
        report = inventory.import_data(file_path, report_type)
        sys.stdout.write(report)
        return
    elif(file_format == '.xml'):
        inventory = InventoryRefactor(XmlImporter)
        report = inventory.import_data(file_path, report_type)
        sys.stdout.write(report)
        return
    else:
        sys.stderr.write("Arquivo inválido")
        return
