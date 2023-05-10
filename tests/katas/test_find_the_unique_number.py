import pytest

from katas.find_the_unique_number import find_uniq


@pytest.mark.parametrize("input, expected_output", [
    ([1, 1, 1, 2, 1, 1, 3, 3, 3], 2),
    ([0, 0, 0.55, 0, 0], 0.55),
    ([3, 10, 3, 3, 3], 10),
])
def test_find_uniq(input, expected_output):
    # act
    result = find_uniq(input)

    # assert
    assert result == expected_output
