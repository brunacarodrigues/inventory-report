from inventory_report.product import Product


def test_product_report() -> None:
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

    assert str(instance_product) == (
        "The product 1 - rubber ducky with serial number 159753 "
        "manufactured on 2020-09-05 by the company toys valid "
        "until 2023-09-05 must be stored according to the "
        "following instructions: dry after use."
    )
