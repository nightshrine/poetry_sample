import pytest
from app.definition.data import Part
from app.services.sum_price import get_parts_sum_price


# 複数のテストケースを定義
@pytest.fixture(
    params=[
        (
            [
                Part(
                    part_id="1",
                    part_name="part_name1",
                    part_quantity=1,
                    part_cost=1000,
                ),
                Part(
                    part_id="2",
                    part_name="part_name2",
                    part_quantity=3,
                    part_cost=300,
                ),
            ],
            1900,
        ),
        (
            [
                Part(
                    part_id="1",
                    part_name="part_name1",
                    part_quantity=2,
                    part_cost=500,
                ),
                Part(
                    part_id="2",
                    part_name="part_name2",
                    part_quantity=4,
                    part_cost=200,
                ),
            ],
            1800,
        ),
        (
            [
                Part(
                    part_id="1",
                    part_name="part_name1",
                    part_quantity=5,
                    part_cost=100,
                ),
                Part(
                    part_id="2",
                    part_name="part_name2",
                    part_quantity=2,
                    part_cost=300,
                ),
                Part(
                    part_id="3",
                    part_name="part_name3",
                    part_quantity=1,
                    part_cost=700,
                ),
            ],
            1800,
        ),
    ]
)
def parts_data(request: pytest.FixtureRequest) -> tuple[list[Part], int]:
    """テスト用の部品データと合計金額を提供するフィクスチャ"""
    return request.param


def test_parts_sum(parts_data: tuple[list[Part], int]):
    """部品の合計金額を取得する"""
    parts, expected_sum = parts_data
    sum_price = get_parts_sum_price(parts)
    assert sum_price == expected_sum
