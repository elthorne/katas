import pytest

from katas.odd_or_even import odd_or_even


@pytest.mark.parametrize("input_array", [
    [0],
    [0, -1, -5],
    [0, 1, 3],
    [1023, 1, 2],
])
def test_odd_or_even_returns_even(input_array):
    # act
    result = odd_or_even(input_array)

    # assert
    assert result == "even"


@pytest.mark.parametrize("input_array", [
    [0, 1, 4],
    [0, 1, 2],
    [0, 1, 6],
])
def test_odd_or_even_returns_odd(input_array):
    # act
    result = odd_or_even(input_array)

    # assert
    assert result == "odd"


def test_odd_or_even_returns_string(input_array):
    # act
    result = odd_or_even(input_array)

    # assert
    assert type(result) == str


@pytest.mark.parametrize("input_array", [
    "foo, bar and things",
    1
])
def test_get_raises_type_error_when_input_is_not_an_int(input_array):
    # arrange, act and assert
    with pytest.raises(TypeError):
        odd_or_even(input_array)
