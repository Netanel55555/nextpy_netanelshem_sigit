def is_funny(string):
    """
        Checks if a string consists only of the letters 'a' and 'h'.

        Args:
            string: The string to be checked.

        Returns:
            True if the string contains only 'a' and 'h', False otherwise.
    """

    return all(char in ('a', 'h') for char in string)


print(is_funny("hahahahahaba"))
