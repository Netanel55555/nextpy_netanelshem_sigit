import functools


def add(x, y):
    """
    Simple function to add two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of the two numbers.
    """
    return x + y


def sum_of_digits(number):
    """
    Calculates the sum of digits in a given number.

    Args:
        number: The number whose digits should be summed.

    Returns:
        The sum of all digits in the number.
    """
    return functools.reduce(add, list(map(int, str(number))))


print(sum_of_digits(104))
