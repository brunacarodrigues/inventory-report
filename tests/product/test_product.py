from inventory_report.product import Product


def test_create_product() -> None:
    product = {
        "id": "1",
        "company_name": "toys",
        "product_name": "rubber ducky",
        "manufacturing_date": "2020-09-05",
        "expiration_date": "2023-09-05",
        "serial_number": "159753",
        "storage_instructions": "dry after use",
    }

    instance_product = Product(**product)

    assert instance_product.id == "1"
    assert instance_product.company_name == "toys"
    assert instance_product.product_name == "rubber ducky"
    assert instance_product.manufacturing_date == "2020-09-05"
    assert instance_product.expiration_date == "2023-09-05"
    assert instance_product.serial_number == "159753"
    assert instance_product.storage_instructions == "dry after use"
