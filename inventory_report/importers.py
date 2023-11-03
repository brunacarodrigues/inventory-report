from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as json_file:
            data = json.load(json_file)
            return [Product(**product) for product in data]


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path) as file:
            data = csv.DictReader(file)

            products = [Product(**item) for item in data]

        return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
