from app.app1 import app1
from app.definition.data import ProductParts
from app.services.sum_price import get_parts_sum_price


def get_product_parts() -> ProductParts:
    """製品と部品リストを取得"""
    product_parts: ProductParts = {
        "product_id": "product_id",
        "product_name": "product_name",
        "parts": [
            {
                "part_id": "1",
                "part_name": "part_name1",
                "part_quantity": 1,
                "part_cost": 1000,
            },
            {
                "part_id": "2",
                "part_name": "part_name2",
                "part_quantity": 3,
                "part_cost": 300,
            },
        ],
    }
    return product_parts


def app2():
    product_parts: ProductParts = get_product_parts()
    parts_sum_price = get_parts_sum_price(product_parts["parts"])
    print("parts_sum_price:", parts_sum_price)
    # 親の関数を呼び出せる
    app1(product_parts)


if __name__ == "__main__":
    app2()
