from app.definition.data import ProductParts


def app1(product_parts: ProductParts) -> None:
    print("product_id:", product_parts["product_id"])
    print("product_name:", product_parts["product_name"])
    print()
    for part in product_parts["parts"]:
        print("part_id:", part["part_id"])
        print("part_name:", part["part_name"])
        print("part_quantity:", part["part_quantity"])
        print("part_cost:", part["part_cost"])
        print()
