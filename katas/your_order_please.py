"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

"""


class UnorderedSentence:
    def __init__(self, sentence: str):
        self.list = sentence.split()
        self.length = len(self.list) + 1


class Words:
    def __init__(self, unordered_sentence: UnorderedSentence):
        self.unordered_sentence = unordered_sentence
        self.ordered_list_of_words = []
        self.ordered_sentence = ""

        self.__orderize()
        self.__format_output()

    def __orderize(self):
        for number in range(self.unordered_sentence.length):
            self.__generate_ordered_list_of_words(number)

    def __generate_ordered_list_of_words(self, number):
        for word in self.unordered_sentence.list:
            self.__append_ordered_word(number, word)

    def __append_ordered_word(self, number, word):
        if str(number) in word:
            self.ordered_list_of_words.append(word)

    def __format_output(self):
        self.ordered_sentence = " ".join(self.ordered_list_of_words)


def order(sentence):
    return Words(UnorderedSentence(sentence)).ordered_sentence
