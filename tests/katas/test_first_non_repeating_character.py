import pytest

from katas.first_non_repeating_character import first_non_repeating_letter


@pytest.mark.parametrize("input_string, expected_value", [
    ("a", "a"),
    ("stress", "t"),
    ("sTreSS", "T"),
    ("moonmen", "e"),
    ("", ""),
    ("abba", ""),
    ("", ""),
    ("~><#~><", "#"),
    ("hello world, eh?", "w"),
    ("Go hang a salami, I\'m a lasagna hog!", ","),
])
def test_first_non_repeating_letter_returns_expected_value(input_string, expected_value):
    # act
    result = first_non_repeating_letter(input_string)

    # assert
    assert result == expected_value
