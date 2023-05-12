import pytest

from katas.the_hashtag_generator import generate_hashtag


@pytest.mark.parametrize("input_string, expected", [
    (" Hello there thanks for trying my Kata", "#HelloThereThanksForTryingMyKata"),
    ("    Hello     World   ", "#HelloWorld"),
    ("", False),
])
def test_generate_hashtag_returns_expected(input_string, expected):
    # act
    result = generate_hashtag(input_string)

    # assert
    assert result == expected
