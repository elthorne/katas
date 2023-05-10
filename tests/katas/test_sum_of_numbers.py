import pytest

from katas.sum_of_numbers import get_sum


@pytest.mark.parametrize("input_1, input_2, expected_output", [
    (1, 0, 1),
    (1, 2, 3),
    (0, 1, 1),
    (1, 1, 1),
    (-1, 0, -1),
    (-1, 2, 2),
    (2, -1, 2),
])
def test_get_sum_returns_expected_output(input_1, input_2, expected_output):
    # act & assert
    assert get_sum(input_1, input_2) == expected_output


@pytest.mark.parametrize("input_1, input_2", [
    ("1", 1),
    (1, "1"),
])
def test_get_sum_raises_type_error_when_input_is_not_an_int(input_1, input_2):
    # arrange, act and assert
    with pytest.raises(TypeError):
        get_sum(input_1, input_2)


def test_get_sum_returns_integer_type():
    # act
    result = get_sum(1, 2)

    # assert
    assert type(result) == int



