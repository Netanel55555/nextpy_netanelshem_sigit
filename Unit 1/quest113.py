def conditions(num):
    """
    This function checks if a given number (`num`) is divisible by 4.

    Args:
        num: The number to check.

    Returns:
        True if the number is divisible by 4, False otherwise.
    """
    return num % 4 == 0


def four_dividers(number):
    """
    Finds all numbers divisible by 4 within a given range.

    Args:
        number: The upper limit of the range (exclusive).

    Returns:
        A list containing all numbers divisible by 4 from 1 up to (but not including) the given number.
    """
    return list(filter(conditions, range(1,number)))


print(four_dividers(3))
