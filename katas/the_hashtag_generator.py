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


class Hashtag:
    def __init__(self, input_string):
        capitalise = ' '.join(elem.capitalize() for elem in input_string.split())
        result = f"#{capitalise.replace(' ', '')}"

        self.result = result

        if not input_string:
            self.result = False

        if len(capitalise) > 140:
            self.result = False


def generate_hashtag(s):
    return Hashtag(s).result
