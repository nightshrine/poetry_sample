from typing import TypedDict


class Part(TypedDict):
    """部品情報"""
    part_id: str
    part_name: str
    part_quantity: int
    part_cost: int


class ProductParts(TypedDict):
    """製品と部品リスト"""
    product_id: str
    product_name: str
    parts: list[Part]
