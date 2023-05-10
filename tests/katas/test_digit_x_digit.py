import pytest

from katas.digit_x_digit import square_digits


@pytest.mark.parametrize("input_number, expected_output", [
    (765, 493625),
    (0, 0),
])
def test_square_digits_returns_concatenated_squared_result_of_every_digit(input_number, expected_output):
    # act
    result = square_digits(input_number)

    # assert
    assert result == expected_output


def test_square_digits_returns_integer():
    # arrange
    input = 765

    # act
    result = square_digits(input)

    # assert
    assert type(result) == int


def test_square_digits_only_accepts_an_integer():
    # arrange, act and assert
    with pytest.raises(TypeError):
        square_digits("765")
