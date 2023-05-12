"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

"""


class Sentence:
    def __init__(self, sentence: str):
        self.sentence = sentence.split()
        self.total_words = range(len(self.sentence) + 1)

    def order(self):
        ordered_words = []
        for number in self.total_words:
            ordered_words = self.__order_words(ordered_words, number)
        return self.format(ordered_words)

    def __order_words(self, ordered_words: list, number: int):
        for word in self.sentence:
            ordered_words = self.__append_word(number, word, ordered_words)
        return ordered_words

    @staticmethod
    def __append_word(number: int, word: str, ordered_words: list):
        if str(number) in word:
            ordered_words.append(word)
        return ordered_words

    @staticmethod
    def format(ordered_words: list):
        return " ".join(ordered_words)


def order(s: str):
    return Sentence(s).order()
