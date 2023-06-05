"""
Kata link: https://www.codewars.com/kata/52449b062fb80683ec000024

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""


class InvalidHashtag(Exception):
    pass


class InvalidSentence(Exception):
    pass


class Sentence:
    def __init__(self, sentence: str):
        if sentence == "":
            raise InvalidSentence("Input cannot be empty")

        self._sentence = sentence

    def get_words(self):
        return self._sentence.split()


class Hashtag:
    def __init__(self, hashtag):
        if len(hashtag) > 140:
            raise InvalidHashtag(f"Hashtag {hashtag} is greater than 140 characters")
        self._hashtag = hashtag

    def to_string(self):
        return self._hashtag


def create_hashtag(input_sentence: Sentence) -> Hashtag:
    capitalise = ' '.join(elem.capitalize() for elem in input_sentence.get_words())
    result = Hashtag(f"#{capitalise.replace(' ', '')}")

    return result


def generate_hashtag(s: str):
    try:
        return create_hashtag(Sentence(s)).to_string()
    except InvalidHashtag:
        return False
    except InvalidSentence:
        return False
