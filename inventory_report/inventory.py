from inventory_report.product import Product
from typing import Optional, List


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        self._data = data or []

    def add_data(self, data: List[Product]) -> None:
        for product in data:
            self._data.append(product)

    @property
    def data(self) -> List[Product]:
        return self._data
