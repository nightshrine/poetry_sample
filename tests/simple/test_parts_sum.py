def test_parts_sum():
    """部品の合計金額を取得する"""
    from app.definition.data import Part

    parts: list[Part] = [
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
    ]
    from app.services.sum_price import get_parts_sum_price

    sum_price = get_parts_sum_price(parts)
    assert sum_price == 1900
