# First try
import functools


def double_letter(my_str):
    """
    Doubles each letter in a given string.

    Iterates through each character in the string, appending it twice to the result string.
    """
    result = ""
    for char in my_str:
        result += char * 2

    return result


def duplicate_letter(char):
    """
        Helper function to duplicate a single character.
        """

    return char * 2


def double_letter_2(my_str):
    """
        Doubles each letter in a given string using map().

        Applies the `duplicate_letter` function to each character in the string,
        then joins the resulting list of doubled characters into a single string.
        """

    return "".join(map(duplicate_letter, my_str))


print(double_letter_2("python"))

#
