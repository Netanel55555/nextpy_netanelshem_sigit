def is_prime(number):
    """
        Checks if a given number is prime.

        A prime number is a whole number greater than 1 whose only factors are 1 and itself.

        Args:
            number: The number to check for primality.

        Returns:
            True if the number is prime, False otherwise.
    """
    return all([False for i in range(2, number) if number % i == 0]) and not number < 2


print(is_prime(43))
