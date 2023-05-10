import pytest

from katas.detect_pangram import is_pangram


@pytest.mark.parametrize("string", [
    "Foo",
    "This isn't a pangram!",
    "abcdefghijklm opqrstuvwxyz",
    "Aacdefghijklmnopqrstuvwxyz"
    "1234567890",
    "",
])
def test_is_pangram_returns_false_when_given_string_is_not_a_pangram(string):
    # act
    result = is_pangram(string)

    # assert
    assert result is False


@pytest.mark.parametrize("string", [
    "The quick brown fox jumps over the lazy dog",
    "The five boxing wizards jump quickly",
    "Pack my box with five dozen liquor jugs",
    "Amazingly few discotheques provide jukeboxes"
])
def test_is_pangram_returns_true_when_given_string_is_a_pangram(string):
    # act
    result = is_pangram(string)

    # assert
    assert result is True


def test_is_pangram_raises_type_error_when_input_is_not_a_string():
    # arrange, act and assert
    with pytest.raises(TypeError):
        is_pangram(765)
