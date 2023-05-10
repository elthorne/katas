import pytest

from katas.digit_x_digit import square_digits_one_liner, square_digits_verbose_original


def test_square_digits_one_liner_returns_concatenated_squared_result_of_every_digit():
    # arrange
    input = 765

    # act
    result = square_digits_one_liner(input)

    # assert
    assert result == 493625


def test_square_digits_one_liner_returns_0_when_an_input_of_0_is_given():
    # arrange
    input = 0

    # act
    result = square_digits_one_liner(input)

    # assert
    assert result == 0


def test_square_digits_one_liner_returns_integer():
    # arrange
    input = 765

    # act
    result = square_digits_one_liner(input)

    # assert
    assert type(result) == int


def test_square_digits_one_liner_only_accepts_an_integer():
    # arrange, act and assert
    with pytest.raises(TypeError):
        square_digits_one_liner("765")


def test_square_digits_verbose_returns_concatenated_squared_result_of_every_digit():
    # arrange
    input = 765

    # act
    result = square_digits_verbose_original(input)

    # assert
    assert result == 493625
