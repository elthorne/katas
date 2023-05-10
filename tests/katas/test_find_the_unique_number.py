import pytest

from katas.find_the_unique_number import find_uniq


@pytest.mark.parametrize("input_array, expected_output", [
    ([1, 1, 1, 2, 1, 1, 3, 3, 3], 2),
    ([0, 0, 0.55, 0, 0], 0.55),
    ([3, 10, 3, 3, 3], 10),
])
def test_find_uniq(input_array, expected_output):
    # act
    result = find_uniq(input_array)

    # assert
    assert result == expected_output


def test_find_uniq_raises_a_type_error_when_input_is_not_an_array():
    # arrange, act and assert
    with pytest.raises(TypeError):
        find_uniq("foo")


def test_find_uniq_returns_integer():
    # act
    result = find_uniq([3, 10, 3])

    # assert
    assert type(result) == int
