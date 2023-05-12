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
    def __init__(self, sentence):
        self.sentence = sentence.split()
        if not sentence:
            self.sentence = ""


def order(s):
    unordered_words = Sentence(s).sentence
    ordered_words = []

    for count in range(len(unordered_words) + 1):
        ordered_words = order_words(ordered_words, unordered_words, count)

    return " ".join(ordered_words)


def order_words(ordered_words, unordered_words, count):
    for word in unordered_words:
        ordered_words = append_word(count, word, ordered_words)
    return ordered_words


def append_word(count, word, ordered_words):
    if str(count) in word:
        ordered_words.append(word)
    return ordered_words
