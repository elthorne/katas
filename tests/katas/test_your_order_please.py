import pytest

from katas.your_order_please import order


@pytest.mark.parametrize("input_string, expected_result", [
    ("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
    ("4of Fo1r pe6ople g3ood th5e the2", "Fo1r the2 g3ood 4of th5e pe6ople"),
    ("", ""),
])
def test_order(input_string, expected_result):
    # act
    result = order(input_string)

    # assert
    assert result == expected_result
