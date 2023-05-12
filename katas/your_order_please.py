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
        self.total = range(len(self.sentence) + 1)

        if not sentence:
            self.sentence = ""

    @staticmethod
    def to_string(ordered_words: list):
        return " ".join(ordered_words)

    def order_words(self, unordered_words: list):
        ordered_words = []
        for count in self.total:
            ordered_words = self.__append_word(ordered_words, unordered_words, count)
        return ordered_words

    def __append_word(self, ordered_words: list, unordered_words: list, count: int):
        for word in unordered_words:
            ordered_words = self.__find_word(count, word, ordered_words)
        return ordered_words

    @staticmethod
    def __find_word(count: int, word: str, ordered_words: list):
        if str(count) in word:
            ordered_words.append(word)
        return ordered_words


def order(s: str):
    words = Sentence(s)

    unordered_words = words.sentence
    ordered_words = words.order_words(unordered_words)

    return words.to_string(ordered_words)
