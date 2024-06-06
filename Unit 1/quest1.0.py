def combine_coins(coin, numbers):
    """Creates a comma-separated string by combining a coin symbol with numbers from a range."""
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '

    return output[:-2]


print(combine_coins('$', range(5)))


