"""
Welcome. In this kata, you are asked to square_each every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!
    :return:
"""


def square_digits(input_number: int):
    if type(input_number) != int:
        raise TypeError("Input number must be an int")

    return int("".join(map(str, [int(digit) ** 2 for digit in str(input_number)])))
