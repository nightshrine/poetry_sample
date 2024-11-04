from app.definition.data import Part


def get_parts_sum_price(parts: list[Part]) -> int:
    sum_price = 0
    for part in parts:
        sum_price += part["part_cost"] * part["part_quantity"]
    return sum_price
